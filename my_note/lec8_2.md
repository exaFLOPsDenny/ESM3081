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

**Goal: Find r-dim projection that best preserves variance (r <= d>)** 

1. Given dataset D = {x_1, x_2,..., x_n} assume or make(StandardScaling) mean of x to 0  
<img width="764" alt="image" src="https://github.com/user-attachments/assets/6ca1f365-345f-4667-bbf6-2e2690df22fa">
<img width="760" alt="image" src="https://github.com/user-attachments/assets/51a6bc21-bcd4-438d-82b5-0b13bd069778">
<img width="764" alt="image" src="https://github.com/user-attachments/assets/4297ace3-f981-4379-8ceb-e6a30d6f5819">  

2. Compute covariance matrix **S** of original data points in the training dataset D 
3. Compute eigenvectors and eigenvalues of **S**
4. Select top r eigenvectors u_1, ..., u_r corresponding to the largest eigenvalues
5. Project each data point onto subspace spanned by selected eigenvectors



