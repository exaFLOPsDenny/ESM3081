## Unsupervised Learning: Dimensionality Reduction & Visualization
<img width="700" alt="image" src="https://github.com/user-attachments/assets/fdce0d16-841f-414a-a45d-f7bb1423a66f">  
<img width="700" alt="image" src="https://github.com/user-attachments/assets/40a3a987-4c59-4336-8862-645ed255037b">

> Linear Dimensionality Reduction vs Nonlinear can't be answered by data scientist but by domain experts.  

### (Projection) Principal Commponent Analysis (PCA)

> PCA is a method that rotates the dataset in a way such that the rotated features are statistically uncorrelated. It reduces a set of features by removing the overlap of information between the original features.

#### New features Z

- **Linear combinations** of the original features(t-SNE is non-linear)  
- uncorrelated  
- Directions of linear combinations are called principal components  

<img width="380" alt="image" src="https://github.com/user-attachments/assets/48911c5f-d477-4605-969e-daba3cc6e10f">

#### Mathematical Interpretation of PCA

**Goal: Find r-dim projection that best preserves variance (r <= d)** 

1. Given dataset D = {x_1, x_2,..., x_n} assume or make(StandardScaling) mean of x to 0  
<img width="700" alt="image" src="https://github.com/user-attachments/assets/6ca1f365-345f-4667-bbf6-2e2690df22fa">

2. Compute covariance matrix **S** of original data points in the training dataset D 
<img width="500" alt="image" src="https://github.com/user-attachments/assets/51a6bc21-bcd4-438d-82b5-0b13bd069778">

3. Compute eigenvectors and eigenvalues of **S**
4. Select top r eigenvectors u_1, ..., u_r corresponding to the largest eigenvalues
<img width="500" alt="image" src="https://github.com/user-attachments/assets/4297ace3-f981-4379-8ceb-e6a30d6f5819">  

5. Project each data point onto subspace spanned by selected eigenvectors

> Eigendecomposition of the covariance matrix of the data

<img width="300" alt="image" src="https://github.com/user-attachments/assets/e0c23001-dd69-4cfd-98a0-a81f9004ae49">

- Finding the eigenvectors with the largest eigenvalues  
    - Eigenvectors - principal components  
    - Eigenvalues - variances explained by principal components  


#### About Principal Component

- The less # of eigenvector, the more it is compressed(Dimension reduction). And the more it loses it's variance(information).  

<img width="500" alt="image" src="https://github.com/user-attachments/assets/4a91421d-63d0-49c9-8047-3f37564ea49d">  

- Default in scikit-learn, pca=PCA() results in no dimension reduction!  
<img width="500" alt="image" src="https://github.com/user-attachments/assets/4ac07b15-271a-430a-89dd-5a1d50fb6aa9">

- Direction (sign) of PC doesn't matter
- Explaning the mixture of features in new PC is tricky   

<img width="500" alt="image" src="https://github.com/user-attachments/assets/bd8364ca-75d9-4d9b-b6bc-3364e0672cc6">
<img width="500" alt="image" src="https://github.com/user-attachments/assets/d39d951d-6b21-46bb-bce6-4411e91c866f">
