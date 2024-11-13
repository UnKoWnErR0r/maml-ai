from flask import Flask, request, jsonify
from model import get_model, load_model
import os

app = Flask(__name__)

# Load the model at the start
model = load_model()

@app.route('/')
def home():
    return "Welcome to the Flask AI App! Your model is ready."

@app.route('/predict', methods=['POST'])
def predict():
    """ Endpoint to make predictions using the model """
    # Check if an image file is included in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No image file in request'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    # Process the image and make prediction
    try:
        # Assuming the image is being sent as a file and needs to be processed
        from PIL import Image
        from io import BytesIO

        # Open the image and prepare it for the model
        img = Image.open(BytesIO(image_file.read())).convert('RGB')

        # Perform inference using Fastai model
        pred, pred_idx, probs = model.predict(img)

        # Return the prediction as a JSON response
        response = {
            'prediction': pred,
            'probabilities': probs.tolist()  # Convert the tensor to a list for JSON compatibility
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/train', methods=['POST'])
def train():
    """ Endpoint to trigger model training """
    try:
        from model import train_model

        # Re-load and train the model
        model = get_model()  # Get a fresh model instance
        train_model(model)   # Train the model
        return jsonify({'message': 'Model is being trained successfully!'})
    except Exception as e:
        return jsonify({'error': f"Training failed: {str(e)}"}), 500

if __name__ == '__main__':
    # Set environment to run on any available network interface
    app.run(host='0.0.0.0', port=5000, debug=True)
