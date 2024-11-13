# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the timezone to New York (Eastern Time)
RUN apt-get update && apt-get install -y tzdata && ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

# Set the working directory
WORKDIR /workspace

# Copy the requirements.txt file into the container
COPY requirements.txt /workspace/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask's default port
EXPOSE 5000
