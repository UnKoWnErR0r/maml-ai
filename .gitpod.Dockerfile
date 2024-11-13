# Use the official Python base image
FROM python:3.12.6

# Set environment variables to non-interactive for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Switch to root user to install system packages
USER root

# Update the apt package list and install tzdata for time zone configuration
RUN apt-get update && apt-get install -y tzdata \
    && ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

# Install Python dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /workspace/

# Expose Flask's default port (5000)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
