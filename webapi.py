from flask import Flask, jsonify, request
import torch, io
import torchvision
import torchvision.transforms as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from PIL import Image
import torchvision.transforms as transforms

# Define the transforms to apply to input images
transform = transforms.Compose([
    transforms.Resize((32,32)),
    transforms.ToTensor(),
    transforms.Normalize([0.8444, 0.8403, 0.8390], [0.2176, 0.2225, 0.2245])
])

class FurnitureNet(nn.Module):
    def __init__(self):
        super(FurnitureNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 3)
        
    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Load the PyTorch model weights
model = FurnitureNet()
model.load_state_dict(torch.load('furniture_model.pth'))
model.eval()

# Create a Flask app
app = Flask(__name__)

# Define the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    image_data = request.files['file'].read()
    image = Image.open(io.BytesIO(image_data))

    # Preprocess the input data
    input_data = transform(image).unsqueeze(0)

    # Make a prediction using the model
    output = model(input_data)
    _, predicted = torch.max(output.data, 1)
    
    item = "no idea"
    if predicted.item()==0:
        item = "Bed"
    elif predicted.item()==1:
        item = "Chair"
    elif predicted.item()==2:
        item = "Sofa"

    # Convert the prediction to a JSON response
    response = {'output': item}
    return jsonify(response)

# Start the Flask app
if __name__ == '__main__':
    app.run()