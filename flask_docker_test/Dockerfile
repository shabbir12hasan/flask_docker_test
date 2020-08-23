# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

# Copy application SRC and Binaries
COPY ./src /opt/src
COPY ./src/ app 
WORKDIR /app

EXPOSE 5001

CMD ["python","app.py","--host", "0.0.0.0"]
