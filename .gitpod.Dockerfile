# Use the official Ubuntu image as the base
FROM ubuntu:20.04

# Install dependencies (e.g., Python 3.9)
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3.9-dev \
    python3.9-distutils \
    python3-pip

# Upgrade pip
RUN python3.9 -m pip install --upgrade pip

# Set the working directory for your project in the container
WORKDIR /workspace

# Copy the requirements.txt to the container
COPY requirements.txt /workspace/

# Install Python dependencies from requirements.txt
RUN python3.9 -m pip install -r requirements.txt  # Install dependencies

# Expose Flask's default port
EXPOSE 5000

# Set the working directory for your project in the container
WORKDIR /workspace
