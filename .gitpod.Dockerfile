# .gitpod.Dockerfile
FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y \
    && apt-get clean

# Set up environment
WORKDIR /workspace
