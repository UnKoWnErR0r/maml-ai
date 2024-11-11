# Use Gitpod's full workspace image as a base
FROM gitpod/workspace-full

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip  # Update pip to the latest version
RUN pip install -r requirements.txt  # Install dependencies

# Expose Flask's default port
EXPOSE 5000

# Set the working directory for your project in the container
WORKDIR /workspace
