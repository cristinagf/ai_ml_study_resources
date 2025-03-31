# Convolutional Neural Networks

Practice notebooks:
  1. Convolutional Neural Networks
  2. Activation functions and Max Polling
  3. Multi-input and output channels
  4. CNN applied: Example
  5. CNN applied: Image/ MNIST
  6. CNN applied: Batch normalization
  7. Torch vision models
  8. Graphic processing unit (GPU)


## Relevant
`convolution` Convolution is a linear operation similar to a linear equation, dot product, or matrix multiplication. Convolution has several advantages for analyzing images, it preserves the relationship between elements, and it requires fewer parameters than other methods.

Relationship between the different functions:
$$linear \ equation :y=wx+b$$
$$linear\ equation\ with\ multiple \ variables \ where \ \mathbf{x} \ is \ a \ vector \ \mathbf{y}=\mathbf{wx}+b$$
$$ \ matrix\ multiplication \ where \ \mathbf{X} \ in \ a \ matrix \ \mathbf{y}=\mathbf{wX}+\mathbf{b} $$
$$\ convolution \ where \ \mathbf{X} \ and \ \mathbf{Y} \ is \ a \ tensor \  \mathbf{Y}=\mathbf{w}*\mathbf{X}+\mathbf{b}$$
In convolution we call w the `kernel`. 


kernel   transformation of input
         its result is knows as the `activation map`

`*`      convolution operation

how to determine size of activ map?
 |input| 4x4 (M), |kernel| 2x2 (K)
- M-K = # of steps
- `stride`  The step-size of the kernel along input
- Size of activ.map: (M-K)/stride + 1. If set to none, shift is the size of K
- `padding` Adding cols/rows to input for processing. Imagine a border around the input image

`max_pooling` Choose max value in region, instead of sum. Reduce size of act-maps, reducing # of parameters. It reduces the impact of small changes on the image  (e.g., recognizing shifting images)

nn.Conv2d (in_channels, out_channels, kernel_size)