from flask import Flask, jsonify, request
from train import train_model
from fastai.data.block import DataBlock
from fastai.vision.data import ImageBlock, CategoryBlock
from fastai.data.transforms import RandomSplitter

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train():
    # Trigger the training process (adjust as needed for your dataset)
    path_to_data = "./data"  # Adjust this path to your data location
    dls = ImageDataLoaders.from_folder(path_to_data, valid_pct=0.2, item_tfms=Resize(224))

    # Start training the model
    train_model(dls)
    
    return jsonify({"message": "Training started!"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
