FROM gitpod/workspace-full  # Use Gitpod's full workspace as a base image

# Install Python dependencies
RUN pip install --upgrade pip  # Update pip to the latest version
RUN pip install -r requirements.txt  # Install dependencies from requirements.txt

# Expose Flask default port
EXPOSE 5000

# Set the working directory to `/workspace`
WORKDIR /workspace
