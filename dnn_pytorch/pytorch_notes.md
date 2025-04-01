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
model.activations   Activation functions

nn.Linear	apply a linear transformation to the input
nn.Sequential   A sequential container. Define NNs
nn.Module   Base module for NN modules; automatize NN creation
nn.ModuleList() Holds submodules in a list. Layers can be appended.
nn.Dropout(p=p) Dropout method
nn.CrossEntropyLoss


torch.optim.ADAM     Method for stochastic optimization: ADAM
torch.relu(Z) | nn.ReLU()
F.relu() (which is torch.nn.functional.relu()) is a function. nn.ReLU (torch.nn.ReLU) is a class that simply calls F.relu(). These two ways of packaging the function do the same thing, including when calling .backward().

# Data
train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=2000, shuffle=True)  Data loader
plt.imshow(data_sample[0].numpy().reshape(IMAGE_SIZE, IMAGE_SIZE), cmap='gray')

# Initialization
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
optimizer = torch.optim.SGD(model_Xavier.parameters(), lr=learning_rate)
optimizer = torch.optim.SGD(model_Uniform.parameters(), lr=learning_rate)
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate, momentum=m)

# Batch normalization
nn.BatchNorm1d  Apply Batch Normalization over a 2D or 3D input

# torch
torch.zeros(M,N)
torch.ones(M,N)
torch.tensor([1,2,3])
torch.Tensor.size(M)    tensor size

# pretrained
model = models.resnet18(pretrained=True)
needs model.train() for training

When using a pre-trained model in PyTorch, setting requires_grad = False for most layers freezes their weights, preventing them from being updated during backpropagation. This is useful in transfer learning, where we use the pre-trained features and only fine-tune specific layers (e.g., the final classifier

# GPU
torch.cuda.is_available()
torch.device('cuda:0')
torch.tensor([1,2,3]).to(device)  `to` method performs device conversion
model = CNN(); model.to(device)   Assign model to GPU
to train first send features and labels to GPU
feature.to(device)  labels.to(device)