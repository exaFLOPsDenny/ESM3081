## Neural Network

Structure
> Input layer : Each input unit represents an input feature  
> Hidden Layer(s) : Each hidden unit represents an intermediate processing step  
> Output Layer : Output unit represents the prediction of the target label  
> Connecting lines: learnable parameters  

#### Non-linear activation function

> Computing a series of weighted sums **without** non-linear activation function is mathematically the same as a linear model.

1. RELU (rectifying nonlinear unit)
    - <code>g(z) = max(0, z)</code>
    - Cuts off values below zero
2. tanh (hyperbolic tangent)
    - <code>g(z) = tanh(z) = (e^z - e^{-z}) / (e^z + e^{-z})</code>
    - Squashes values between -1 and 1

