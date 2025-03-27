# Cross Entropy Loss

When training classifiers, we aim to minimizing the number of misclassified samples.
This translate into minimizing the loss or cost function.

## Loss
Theshold based loss:
    l(b) = sumn=1..N (yn - THR(xn + b))2
Sigmoid based loss:
    Loss surface better, but at some regions it could lead to no update. 
For example, if initialized at one of these flat regions. 
Maximum Likelihood:
    Inv Log of a peak curve, averaged over N. Min of resulting curve, corresponds to max likelihood
Cross Entropy Loss
    Contour plot shows only flat at the minimum.


Logistic regression:
1) Create the model z= xw + b2) 
   a) model == nn.Sequential(nn.Linear*1,1), nn.Sigmoid()) -> Produce 1-dim output
   b) Define custom model by  nn.Module
```python
       class log_ref(nn.Module):
          def __init(self, input_dim, output_dim):
          // initialization 
         def forward(self, input):
          //calculate output based on input
           // e.g. sigmoid
           def criterion(Y, y):
           // nn.MSELoss() or nn.BCELoss
```

Implementation:
1) Load data: trainloader = DataLoader(dataset, batch_size)
2) Create Model: model = log_ref() // our model
   and optimizer:
optimizer = optim.SGD(model.parameters(), lr=0.01)
3) Train:
for epoch in range(100):
  for x,y in trainloader:
    y_hat = model(x)
    loss = criterion(y_hat, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    // output will have a value between 0-1. We need thresholding to final labels.


Notes:
- The backward function, in the context of PyTorch's logistic regression, computes the gradients of the loss with respect to the model parameters. This is important for the parameter update step.
- Once the gradients are computed, you use an optimizer to update the model parameters based on these gradients. The optimizer adjusts the parameters in the direction that reduces the loss, using the computed gradients. 


