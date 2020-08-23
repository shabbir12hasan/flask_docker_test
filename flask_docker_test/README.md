### Python flask app and dockers

1. Creating a hello-world flask app
2. Creating a docker image


#### 1. Flask app
- Building a hello world app, naming it as app.py
- Creating an HTML template and placing inside templates folder
- setting host and port name in the app

#### 2. Creating a docker image
- Docker setup is important (which is not covered here)
- Command to build the docker image: "docker build -t imagename ."
- Command to run the docker: "docker run -p 5001:5001 -d imagename"

##### Then use postman to check if the get request is working, using 0.0.0.0:5001