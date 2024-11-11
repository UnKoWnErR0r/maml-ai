import torch
import torch.nn as nn
from fastai.vision.all import *
from fastai.callback.core import Callback
import yaml

# Load configuration from config.yaml
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

inner_lr = config['meta_learning']['inner_lr']
meta_lr = config['meta_learning']['meta_lr']
epochs = config['meta_learning']['epochs']

# Define a custom meta-learning model using ResNet18
class MetaModel(nn.Module):
    def __init__(self, num_classes=5):
        super(MetaModel, self).__init__()
        self.resnet = models.resnet18(pretrained=True)  # A pretrained ResNet
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, num_classes)

    def forward(self, x):
        return self.resnet(x)

# Custom Callback for Meta-Learning (MAML)
class MetaLearner(Callback):
    def __init__(self, model, meta_lr=0.001, inner_lr=0.01):
        self.model = model
        self.meta_lr = meta_lr
        self.inner_lr = inner_lr

    def before_fit(self):
        self.inner_optimizer = torch.optim.SGD(self.model.parameters(), lr=self.inner_lr)

    def before_batch(self):
        # Save original model parameters for meta-gradient computation
        self.original_params = {name: param.clone() for name, param in self.model.named_parameters()}

    def after_batch(self):
        # Perform the inner-loop update (task-specific adaptation)
        self.inner_optimizer.zero_grad()
        loss = self.learn.loss_func(self.pred, self.yb)
        loss.backward()
        self.inner_optimizer.step()

    def after_epoch(self):
        # Compute the meta-gradient (outer-loop update)
        meta_optimizer = torch.optim.Adam(self.model.parameters(), lr=self.meta_lr)
        meta_optimizer.zero_grad()
        for name, param in self.model.named_parameters():
            # Compute meta-gradient by comparing with the original params
            param.grad = (param - self.original_params[name]).detach()
        meta_optimizer.step()
        self.model.train()  # Ensure the model is in training mode after each update

# Main function to create the learner and train the model
def train_model(dls):
    model = MetaModel(num_classes=5)  # Customize based on your task
    learner = cnn_learner(dls, model, metrics=accuracy, cbs=[MetaLearner(model, meta_lr, inner_lr)])
    learner.fit_one_cycle(epochs)  # Train for the specified number of epochs

if __name__ == "__main__":
    # Example of using a DataLoader (assuming you have a dataset ready)
    # Modify this to your dataset path and configuration
    path_to_data = "./data"  # Adjust this path accordingly
    dls = ImageDataLoaders.from_folder(path_to_data, valid_pct=0.2, item_tfms=Resize(224))

    train_model(dls)  # Start training the model

