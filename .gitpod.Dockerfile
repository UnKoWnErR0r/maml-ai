# Use the Gitpod base workspace image
FROM gitpod/workspace-full

# Set the time zone to Eastern Time (New York)
USER root  # Switch to root user to run system-level commands
RUN apt-get update && apt-get install -y tzdata \
    && ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

# Install Python dependencies from requirements.txt
COPY requirements.txt /workspace/
RUN pip install --upgrade pip  # Upgrade pip first
RUN pip install -r /workspace/requirements.txt  # Install dependencies

# Expose Flask's default port
EXPOSE 5000

# Set the working directory for your project in the container
WORKDIR /workspace

# Copy the project files into the container
COPY . /workspace/

# Run Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
