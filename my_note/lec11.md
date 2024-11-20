## Feature Engineering
> Feature Engineering is questioning how to represent data the best

- While tree-based models only care about the ordering of the features, most of the 
other models including linear models and neural networks are very tied to the scale and distribution of each feature

### Categorical Features

- Too small categories can be merged
<img width="300" alt="image" src="https://github.com/user-attachments/assets/4afa6b0d-3a65-42b6-8ac0-28c6837e2fc4">

- Even for numerical type, if it is categorical feature, need to be included in dummy feature
<img width="500" alt="image" src="https://github.com/user-attachments/assets/2bc07dc5-d7ac-4e04-9b12-3e325bbe5f1c">

- Mostly one-hot encoding 

### Binning (Discretization)
> Binning is to discretize feature so it can split into multiple features
<img width="500" alt="image" src="https://github.com/user-attachments/assets/1941fc43-4021-4277-b553-9d0b7dd8519e">

- Linear models benefit greatly in expressiveness from binning of continuous features
- No effect for DT, as it is doing the best binning(multiple feature + split anywhere the best)
- No big effect on Non-linear model 

### Polynomials and Interactions
> Polynomials can be added to enrich feature representation

<img width="500" alt="image" src="https://github.com/user-attachments/assets/e16b1e80-6556-40d1-8434-b10f8743d455">

- degree
    - Too high ~ overfitting 
- interaction_only
    - If True: no product with other features
- include bias
    - If True: bias is added
    - **Logistic regression needs to be False** as bias is already embedded
- No big effect on Non-linear model 

### Univariate Nonlinear Transformations
> Trying to make the model distribution as Gaussian distribution

- Logarithmic Transformation
<img width="469" alt="image" src="https://github.com/user-attachments/assets/cb7dcd4a-51b8-4df5-879c-125c7b3a9899">

- Each feature needs to be transformed in a different way
- Right-skewed distribution use log(y+1) transformation
- Univariate nonlinear transformation irrelevent for tree-based model
- Also for target y in regression can help

## Automatic Feature Selection
> Feature Engineering tends to increase the dimensionality making it more complex.  
> Feature selction is to reduce # of features.

- Feature Extraction vs Feature Selection
    - Feature Extraction seems more efficient
    - When Feature selection is used
        - Features are expensive to obtain( by discarding the feature, we don't have to gather the discarded feature data)
        - Interpretability as it preserve original representation

### Filter Methods