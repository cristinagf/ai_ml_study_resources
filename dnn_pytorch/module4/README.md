# Deep Neural Networks

Practice notebooks:
  1. Deep layer Neural Networks (DNN)
  2. DNNs with nn.Module
  3. Dropout: Improve performance of DNNs; preventing overfitting
  
     - Trying combinations of number of layers/neuron can be time-consuming.
     - An option is apply Dropout: start with a complex model, then apply regularization (dropout).
     - During training, we enable dropout. In evaluation, dropout is disabled.
     - Dropout is applied in the forward step. At each iteration, each neuron has a probability p of being shut-off. 
     - p is now a hyperparameter. If too low, we risk overfitting. Too large, risks underfitting.
     - In general, dropout is applied after the non-linear activation function.  However, when using ReLUs, dropout is applied before the activation for computational efficiency (e.g., when using nn.Sequential).

  4. Dropout: Overfitting
  5. Initialization

     - Erroneous evolvement of DNNs may be related to weight initialization for training.
     - Depending on the activation function techniques such as: normalized weights, Xavier, He help avoiding vanishing or exploding gradients
  
  6. Initialization: Xavier
  7. Initialization: He
  8. Gradient descent with Momentum
  9. Batch Normalization


## Relevant
- Use of PyTorch `nn.Module` to automate DNN creation. 
  <a href='https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module'>`nn.Module`</a> provides a base class for all neural network modules.
  
Modules can also contain other Modules, allowing them to be nested in a tree structure. You can assign the submodules as regular attributes:

```python
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        return F.relu(self.conv2(x))
```


