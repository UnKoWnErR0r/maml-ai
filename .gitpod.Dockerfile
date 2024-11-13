# Use the Gitpod base workspace image
FROM gitpod/workspace-full

# Install Python dependencies from requirements.txt
COPY requirements.txt /workspace/

# Install tzdata to configure the time zone and avoid interactive prompts
RUN apt-get update && apt-get install -y tzdata \
    && ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

# Install Python 3 dependencies
RUN pip install --upgrade pip  # Upgrade pip first
RUN pip install -r /workspace/requirements.txt  # Install dependencies

# Expose Flask's default port
EXPOSE 5000

# Set the working directory for your project in the container
WORKDIR /workspace

# Copy your project files into the container (if not already)
COPY . /workspace/

# Run Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
