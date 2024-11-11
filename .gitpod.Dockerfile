FROM gitpod/workspace-full

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set the default working directory
WORKDIR /workspace

# Expose port
