## Neural Network

### Structure
> Input layer : Each input unit represents an input feature  
> Hidden Layer(s) : Each hidden unit represents an intermediate processing step  
> Output Layer : Output unit represents the prediction of the target label  
<img width="700" alt="image" src="https://github.com/user-attachments/assets/70b0fee7-6945-4be8-bb4e-4b9df1230d85">
<img width="700" alt="image" src="https://github.com/user-attachments/assets/ae6eec96-cbc3-4ee5-83b4-440084718ed0">  


- Connecting lines: learnable parameters  
- Pre-processing data scaling is needed for both features and target
- Evaluation is occured after inverse scaling transform.

### Strenghts
- Large data, complex model and good predictive ability

### Weeknesses
- Long time to train
- Tuning hyperparameter is art onto itself
- Black box model

### Non-linear activation function

> Computing a series of weighted sums **without** non-linear activation function is mathematically the same as a linear model.  

<img width="700" alt="image" src="https://github.com/user-attachments/assets/562ee2cc-e652-4f27-9dc7-4448e1c97144">

### Hyperparameters

- Hidden layer sizes (e.g. (50,30,20))
- Activation function
    - tanh and sigmoid are less sensitive to noise
- Alpha for L2 regularization
- Solver (sgd, adam, lbfgs, etc)


#### # parameter w.r.t model complexity
<img width="811" alt="image" src="https://github.com/user-attachments/assets/e196477e-ca9b-46d1-8c65-4c54c341c299">

https://www.nature.com/articles/nature14539




#### Uncertainty Estimates
> High inpurity ~ High uncertainty 

<img width="432" alt="image" src="https://github.com/user-attachments/assets/93973a99-daa8-4f09-aca5-8c7e95a59387">
