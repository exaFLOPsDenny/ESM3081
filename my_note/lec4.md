## Decision Tree

Structure
> A decision tree is a hierarchy of if/else questions leading to a decision built by learning from data  

> Inner node: feature  
> Edge : condtion of a feature value  
> Leaf node: prediction  

- Strength
    - Extracted knowledge can be easily understood, interpreted, controlled by humans in the form of a readable decision tree  
    - By seeing feature importance, we can see which feature is giving big effect  
    - No need of data scaling
    - Feature selection & reduction is automatic
    - robust to outliers
    - Well on mixed type of features  
- Weekness
    - tend to overfit
    - interaction between features are ignored
    - Space of possible DT is large


Finitely many different decision trees can exist. 
- Optimal algorithm: generates all possible trees and choose the best one.
- Heuristic algorithms: with greedy strategy  
### Procedure
1. Repeatedly split a node into two parts so as to minimize the impurity of outcome within the new parts

### How to determine the best split?
- Regression  
    - To **minimize the variance**, but the results for unknown data which might escape the range of train data might be poor.
    - Poor result: mean value of train data
<img width="589" alt="image" src="https://github.com/user-attachments/assets/7f4ec027-0f9a-4227-b139-bf85a926bb02">  

- Classification  
<img width="50%" alt="image" src="https://github.com/user-attachments/assets/a8de12b5-0fbb-4715-9889-62c87a79e998"> <img width="432" alt="image" src="https://github.com/user-attachments/assets/247aa143-57bd-479f-84bd-d2cab33fb14b">

### Problem below
<img width="728" alt="image" src="https://github.com/user-attachments/assets/7cb0997b-dc6b-4a65-99ad-4432ebb3b7bd">

- Very complex, overfitted
- So we can use greedy strategy, and use majority class for Classification, mean target for Regression.  

### Solution  
- Pre-pruning(used more): Stopping the creation of the tree early
    <img width="589" alt="image" src="https://github.com/user-attachments/assets/382de84d-ebea-43a7-88d1-ba45abdbde10">  
    - min_sample_leaf: **small** ~ overfit
    - max_depth: big ~ overfit
    - max_leaf_node: big ~ overfit
- Post-pruning: removing or collapsing nodes that contain little infomation


Decision trees tend to overfit the training data
- Ensemble methods combine multiple machine learning models to create more powerful models.  
<img width="450" alt="image" src="https://github.com/user-attachments/assets/68d43814-3e6f-4b10-8482-f271eb65a5d8">

## Random Forests

> Random forest is an ensemble of decision trees, where each tree is slightly different from others  
> Got it's name by injecting randomness into the tree building to ensure each tree is different. By this, reducing the amount of overfitting by averaging their results while retaining the predictive power of the trees.  
> As admitting there will be overfitting on trees, hyperparameters(max_depth, max_features, n_leaf_nodes) of each trees don't effect that much.  

- Strengths  
    - Powerful ("Do we need hundreds of classifiers to solve real world classification problem? - Are Random Forests truly the best classifiers?)
    - Work well without heavy tuning hyperparameters
- Weakness
    - Impossible to interpret all each trees
    - Time-consuming(no pre-pruning) -> n_jobs

### Randomness
1. Bootstrap (by selecting the data points used to build a tree)
    - slightly different dataset(복원추출)
2. Max_features (by selecting the features in each split test)
    - High: trees will be quite similar to each other
    - Low: different and might need to be deeper
    - Classification($\sqrt{p}$) and Regression(p/3)  
<img width="656" alt="image" src="https://github.com/user-attachments/assets/1a67f0bf-7897-40ec-9fd8-c8ddbeafa620">

### Hyperparameter of Random Forest
- n_estimators: # of trees (more the better but over 128 no much difference)
- max_features
- bootstrap
<img width="795" alt="image" src="https://github.com/user-attachments/assets/4ce67dcd-7910-424e-83d5-4ca7bd8ade2b">

<img width="795" alt="image" src="https://github.com/user-attachments/assets/c9881d91-505b-47e8-b4d1-aca7c83faa5d">
