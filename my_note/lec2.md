## Types of Learning  
- Model-Based Learning (Eager Learning)  
> Training phase: Build a model using training data  
> Prediction phase: Use the model to make predictions  

- Instance-Based Learning (Lazy Learning)  
> Training phase: Do nothing  
> Prediction phase: Compare new instances with training data to make predictions  
> When to use : As it takes less time in training but more on predicting, good for situations when data becomes available gradually over time.   

## k-Nearest Neighbors (KNN)

- Strenghts  
    - No parameters in model, making easy to understand
    - Reasonable performance without a lot of adjustments
- Weaknesses
    - Slow as training set gets larger
    - Poor on dataset with many features
- Algorithm    
    > 1. Compute distance from new instance point x to each data point in <ins>D(distance metric))</ins>
    > 2. Identify <ins>k</ins> nearest neighbors of x
    > 3. Use labels of the nearest neighbors to predict y (weighting scheme)

<img width="637" alt="image" src="https://github.com/user-attachments/assets/1ba15572-c807-4adb-98f0-2c798b96c082">  

> Many algorithms have a classification and a regression variant

## Hyperparameters in KNN
> Chosen to have the highest performance in validation data

### Distance metric
<img width="234" alt="image" src="https://github.com/user-attachments/assets/e6f4a927-3805-4080-9a5f-e9bf7babbc2b">

### k (# of neighbor)

- smaller k : capture local structure in data (but also noise, high model complexity) --> overfitting
- larger k : provide more smoothing, less noise, but may miss local structure (low model complexity) --> underfitting

### Weight function
<img width="495" alt="image" src="https://github.com/user-attachments/assets/6dc091ac-97e5-4fda-b3ea-1709cf097318">

## Preprocessing data

### Data Scaling
<img width="482" alt="image" src="https://github.com/user-attachments/assets/3c6bb057-b03b-4bbd-8811-8035eb668fe5">

### One-Hot Encoding
<img width="493" alt="image" src="https://github.com/user-attachments/assets/dc790602-161c-43d6-afb0-f4427866e433">
