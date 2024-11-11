import torch
import torch.nn as nn
from torchvision import models

class MetaModel(nn.Module):
    def __init__(self, num_classes=5):
        super(MetaModel, self).__init__()
        self.resnet = models.resnet18(pretrained=True)  # A pretrained ResNet
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, num_classes)

    def forward(self, x):
        return self.resnet(x)
