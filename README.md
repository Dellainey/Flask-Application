# Flask-Application

This repository includes a flask application for implementing an NLP task (sentiment analysis).

I have used a simple Logistic Regression model that i had trained some time back. It has been trained on the tweets to classify them into either a positive class (1) or a negative class (0).

So the model takes in a sentence and predicts it to be either '1' or '0'

Feel free to use any other trained models or to perform any other ML task.

The repository includes the following:

    1. app.py
       This is the flask app that will be used to run your trained model and make requests to it. It has a class 'Model' where we define the model and the supporting files if needed (In my case i had a trained vectorizer). I have also defined a 'Prediction' function that vectorizes the message and returns a prediction using our model.

       The app has two endpoints. '/' will only show the landing page, while the '/predict' accepts a POST request in Json format.

       The app will run on localhost on port 8080.

       Note that we load the model just once when the docker image is created, this saves a lot of time especially if the model is very large.

    2. Dockerfile
       I will be running the app in a docker image. You can install the libraries that  your app depends on here.

    3. Makefile
       I love Makefiles, they are so convinient. Here i have the commands to build, run and stop my docker image. You can use them as follows:
       - $ make build       This will build a docker image
       - $ make run         This will spin up the docker container on port 8080
       - $ make stop        This will stop and remove the docker image

    4. post.py
       This is a short script to make a POST request to my app. Feel free to change the input message.

    5. requirements.txt
       This has the dependencies to run our post request. You can create an environment to run the POST request. Note that an environment is not needed to run the app as we run it in the docker.

    6. model folder
       This is used to keep your trained models and any other files needed for your task.   


To run the application follow the below steps:

    - Fork the repository and nevigate to the folder.
    - $ make build
    - $ make run

You can check if your docker container is running by typing 
    
    - $ docker ps

To make post requests to the app, first create a virtual enviroment, activate it and install the dependencies

    - $ python3 -m venv venv
    - $ . venv/bin/activate
    - pip install -r requirements.txt

To test it run the post.py

    - $ python post.py

If everything goes well, this should return either a 1 or 2.

That's it! Now you can build your own apps for the models that you train :) !







