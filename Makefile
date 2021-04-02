build:
	- sudo docker build --network=host -t flask-application:latest .

run:
	- sudo docker run --rm -it --network=host  -p 8080:8080 flask-application 

stop:
	- sudo docker stop flask-application
	- sudo docker rm flask-application


	