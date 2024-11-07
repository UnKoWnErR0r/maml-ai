import torch
import torch.nn as nn
import torch.optim as optim
import torchmeta
from torchmeta.datasets import Omniglot
from torchmeta.utils.data import BatchMetaDataLoader
from model import CNN  # We will define this model next
import yaml

def load_config(config_path="config.yaml"):
    """Load configuration from YAML file."""
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def maml_step(model, data, targets, learning_rate=0.01):
    """Perform a single MAML update step."""
    output = model(data)
    loss = nn.CrossEntropyLoss()(output, targets)
    gradients = torch.autograd.grad(loss, model.parameters(), create_graph=True)
    updated_params = list(map(lambda p: p - learning_rate * g, zip(model.parameters(), gradients)))
    
    # Apply updated params to a new model copy
    model_copy = CNN()
    model_copy.load_state_dict(dict(zip(model.state_dict().keys(), updated_params)))
    
    return model_copy, loss

def train_maml(model, dataloader, num_epochs=10, learning_rate=0.01):
    """Train the model using MAML."""
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    for epoch in range(num_epochs):
        total_loss = 0
        for batch in dataloader:
            support_set, query_set = batch['train'], batch['test']
            data, targets = support_set['image'], support_set['target']
            
            model_copy, loss = maml_step(model, data, targets, learning_rate)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        print(f'Epoch {epoch+1}/{num_epochs}, Loss: {total_loss / len(dataloader)}')

def main():
    # Load configuration
    config = load_config()
    model = CNN(input_channels=1, output_classes=config["model"]["output_classes"])

    # Load the Omniglot dataset
    dataset = Omniglot(root='data', num_classes_per_task=5, num_samples_per_class=5, meta_train=True)
    dataloader = BatchMetaDataLoader(dataset, batch_size=4, shuffle=True)
    
    # Train the model
    train_maml(model, dataloader, num_epochs=10, learning_rate=config["model"]["learning_rate"])

    # Save the model after training
    torch.save(model.state_dict(), "models/maml_model.pth")

if __name__ == "__main__":
    main()
