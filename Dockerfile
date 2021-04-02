
FROM python:3.7-slim

RUN pip install flask gunicorn sklearn
# Copy local code to the container image.
WORKDIR /app

# Copy all the files to the app folder
ADD . .
ENV PORT 8080

# Run the web service on container startup. Here we use gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 1 app:app