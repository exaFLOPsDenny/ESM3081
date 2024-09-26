## Types of Learning  
- Model-Based Learning (Eager Learning)  
> Training phase: Build a model using training data  
> Prediction phase: Use the model to make predictions  

- Instance-Based Learning (Lazy Learning)  
> Training phase: Do nothing  
> Prediction phase: Compare new instances with training data to make predictions  
> When to use : As it takes less time in training but more on predicting, good for situations when data becomes available gradually over time.   

## k-Nearest Neighbors (KNN)

- No parameters in model

> 1. Compute distance from new instance point x to each data point in <ins>D(distance metric))</ins>
> 2. Identify <ins>k</ins> nearest neighbors of x
> 3. Use labels of the nearest neighbors to predict y (weighting scheme)

### hyperparameter k

- smaller k : capture local structure in data (but also noise, high model complexity) --> overfitting
- larger k : provide more smoothing, less noise, but may miss local structure (low model complexity) --> underfitting

### Data scaling
