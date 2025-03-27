## PyTorch: Common commands and elements

model.parameters    check param size
```python
<bound method Module.parameters of Net(
  (hidden): ModuleList(
    (0): Linear(in_features=3, out_features=3, bias=True)
    (1): Linear(in_features=3, out_features=4, bias=True)
    (2): Linear(in_features=4, out_features=3, bias=True)
  )
)>
```
len(self.hidden)    Number of hidden layers
model.eval()    Set model into evaluation mode. E.g., dropout is shut-off
model.state_dict()  Inspect current state of model

nn.Linear	apply a linear transformation to the input
nn.Sequential   A sequential container. Define NNs
nn.Module   Base module for NN modules; automatize NN creation
nn.ModuleList() Holds submodules in a list. Layers can be appended.
nn.Dropout(p=p) Dropout method
nn.CrossEntropyLoss


torch.optim.ADAM    ADAM optimizer

# Data
train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=2000, shuffle=True)  Data loader

# Initialization
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
optimizer = torch.optim.SGD(model_Xavier.parameters(), lr=learning_rate)
optimizer = torch.optim.SGD(model_Uniform.parameters(), lr=learning_rate)
