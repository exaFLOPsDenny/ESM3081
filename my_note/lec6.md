## Neural Network

Structure
> Input layer : Each input unit represents an input feature  
> Hidden Layer(s) : Each hidden unit represents an intermediate processing step  
> Output Layer : Output unit represents the prediction of the target label  
<img width="668" alt="image" src="https://github.com/user-attachments/assets/ae6eec96-cbc3-4ee5-83b4-440084718ed0">  

> Connecting lines: learnable parameters  

- Strenghts
    - Large data, complex model and good predictive ability
- Weeknesses
    - Long time to train
    - Tuning hyperparameter is art onto itself
    - Black box model

### Non-linear activation function

> Computing a series of weighted sums **without** non-linear activation function is mathematically the same as a linear model.  

1. RELU(rectifying nonlinear unit)

    $$ g(z) = max(0,z) $$
    - Cuts off values below zero

2. tanh(hyperbolic tangent)

    $$ g(z) = \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} $$
    - saturates to -1 ~ +1

### Hyperparameters

1. hidden layer sizes (e.g. (50,30,20))
2. activation function
    - tanh and sigmoid are less sensitive to noise
3. alpha for L2 regularization
4. solver (sgd, adam, lbfgs, etc)

- Feature and label both needs to be scaled  
- Evaluation is occured after inverse scaling transform.

#### # parameter w.r.t model complexity
<img width="811" alt="image" src="https://github.com/user-attachments/assets/e196477e-ca9b-46d1-8c65-4c54c341c299">

https://www.nature.com/articles/nature14539




#### Uncertainty Estimates
> High inpurity ~ High uncertainty 

<img width="432" alt="image" src="https://github.com/user-attachments/assets/93973a99-daa8-4f09-aca5-8c7e95a59387">
