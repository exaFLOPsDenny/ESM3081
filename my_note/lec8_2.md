## Unsupervised Learning: Dimensionality Reduction & Visualization

### (Projection) Principal Commponent Analysis (PCA)

> PCA is a method that rotates the dataset in a way such that the rotated features are statistically uncorrelated. It reduces a set of features by removing the overlap of information between the original features.

#### New features Z

- Linear combinations of the original features  
- uncorrelated  
- Directions of linear combinations are called principal components  

<img width="380" alt="image" src="https://github.com/user-attachments/assets/48911c5f-d477-4605-969e-daba3cc6e10f">

#### Mathematical Interpretation of PCA

> Eigendecomposition of the covariance matrix of the data

<img width="169" alt="image" src="https://github.com/user-attachments/assets/e0c23001-dd69-4cfd-98a0-a81f9004ae49">

- Finding the eigenvectors with the largest eigenvalues  
    - Eigenvectors - principal components  
    - Eigenvalues - variances explained by principal components  

** Goal: Find r-dim projection that best preserves variance (r <= d>) ** 

1. Given dataset D = {x_1, x_2,..., x_n} assume or make(StandardScaling) mean of x to 0.  
2. 



