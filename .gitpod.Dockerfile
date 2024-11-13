# Use a generic Python 3.12 image from Docker Hub
FROM python:3.12-slim

# Install required dependencies
RUN apt-get update && apt-get install -y \
    tzdata \
    && ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

# Set working directory
WORKDIR /workspace

# Install Python dependencies from requirements.txt
COPY requirements.txt /workspace/
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask's default port
EXPOSE 5000
