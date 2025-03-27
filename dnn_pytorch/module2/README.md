# SoftMax

The Softmax function is a fundamental component in multi-class classification tasks. 

Softmax converts a vector of real-valued numbers into a probability distribution where: each value is transformed into a probability (ranging from 0 to 1). The probabilities sum to 1 across all classes.

The Softmax function extends logistic regression to handle multiple classes.

## Softmax in 1 dimension

Similar to logistic regression, we will have classes, in this case multiple classes.
Feature vectors or tensors represent the input samples.
Softmax will use multiple linear classifiers.


## Argmax function
The `argmax` returns the index corresponding to the largest value in a sequence.
e.g. 
z = [0 2 4 5 5 2 100]
argmax(z) = 6

## Combining argmax and Softmax
Picture a 2-dimensional space, where input values lie on the x axis. Assume we have 3 different classes, present in different ranges along the x axis. 
If we have 3 linear classifiers, softmax. For each point, we will have an output value given by the classifier.
By applying argmax to such outputs, we'll get the index of the maximum output, which identifies the class.

## Softmax in 2 dimensions
Here each input to be classified is represented by a vector. For example a pixel in a 2-D image.
y = argmax{wx + b}
w characterizes the vector of the classifier.
[zo z1 z2] = [x1 x2] [w1 w2 w3] + [b0 b1 b2]
Actual distance, dot product of each input vector with the parameters, is converted to probabilities using probability functions, similar to logistic regression.

You can visualize Softmax as a multi-output linear regression.
Instead of y, we use z. For classification we are interested in the column indexes associated with the classes.

## Implementation in PyTorch
Use nn.Module:

```python
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self, in_size, num_out_classes):
        super(Softmax, self).__init__()
        self.linear = nn.Linear(in_size, num_out_classes)

    def forward(self, x):
        out = self.linear(x)  # No logistic function
        return out
```

e.g., Image classification
```python
model = Softwmax(2, 3)
x = torch.tensor([[1.0,2.0]])
z = model(x)
output = z.max(1)  # 1: with respect to columns
```
The output is a tensor([1])


## Practice code

See notebooks for Softmax for 1D and 2D input.

