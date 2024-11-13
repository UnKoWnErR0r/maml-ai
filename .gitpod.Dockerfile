FROM python:3.12-slim

RUN apt-get update && apt-get install -y tzdata && ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

WORKDIR /workspace

# Directly install requirements (assuming requirements.txt is already in the workspace)
RUN pip install --no-cache-dir tensorflow==2.14.0 numpy==1.23.5 pyyaml==6.0 matplotlib==3.7.1 scikit-learn==1.2.2

EXPOSE 5000
