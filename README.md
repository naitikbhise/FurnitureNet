# FurnitureNet

## Training the Model
The code for training the model is located in the Untitled.py file. Once you run this file, it will generate the model weights file furniture_model.pth.

## Using the Model
To use the trained model, you can run the webapi.py file, which starts a Flask web server. You can then send POST requests to the server using the request_file.py file, which sends an example image to the server and receives the predicted class.

Alternatively, you can send a POST request to the server using a tool like Postman. To do this, set the request URL to http://localhost:5000/predict, and include a file parameter named file in the request body. The value of this parameter should be the path to the image file on your local machine.

For example, if your image is located at ./Dataset/Bed/Aubree Queen Bed.jpg, the request body would look like this:

{
    "file": "./Dataset/Bed/Aubree Queen Bed.jpg"
}
## Building and Running the Docker Image
To build the Docker image for this project, run the following command in your terminal:


docker build -t my-flask-app .
Once the image is built, you can run it using the following command:

docker run -p 5000:5000 my-flask-app
This will start the Flask web server inside the Docker container, and map port 5000 from the container to port 5000 on your local machine.

## Continuous Integration and Deployment
This project has a GitHub Actions workflow configured for continuous integration and deployment. The workflow is defined in the .github/workflows/main.yml file, and runs whenever a commit is pushed to the main branch.

The workflow consists of two jobs: build and deploy. The build job builds the Docker image for the project, while the deploy job pushes the image to the GitHub Container Registry and deploys it to a remote server.

To use the GitHub Actions workflow for your own deployments, you will need to set up your own remote server and update the workflow file with your server details. You will also need to set up a personal access token in your GitHub account and add it as a secret to your repository, so that the workflow can authenticate with the GitHub Container Registry.
