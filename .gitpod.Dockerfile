FROM gitpod/workspace-python3:latest

# Install TensorFlow and other dependencies
RUN pip install --upgrade pip
RUN pip install tensorflow==2.14.0 numpy==1.23.5 pyyaml==6.0 matplotlib==3.7.1 scikit-learn==1.2.2

# Set working directory
WORKDIR /workspace

# Expose Flask's default port
EXPOSE 5000
