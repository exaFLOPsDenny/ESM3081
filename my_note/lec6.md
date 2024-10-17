## Neural Network

Structure
> Input layer : Each input unit represents an input feature  
> Hidden Layer(s) : Each hidden unit represents an intermediate processing step  
> Output Layer : Output unit represents the prediction of the target label  
<img width="668" alt="image" src="https://github.com/user-attachments/assets/ae6eec96-cbc3-4ee5-83b4-440084718ed0">
> Connecting lines: learnable parameters  

#### Non-linear activation function

> Computing a series of weighted sums **without** non-linear activation function is mathematically the same as a linear model.  

1. RELU(rectifying nonlinear unit)

    $$ g(z) = max(0,z) $$
    - Cuts off values below zero

2. tanh(hyperbolic tangent)  

    $$ g(z) = \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} $$  
    - saturates to -1 ~ +1

