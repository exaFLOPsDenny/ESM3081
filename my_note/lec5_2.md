# Support Vector Machines (SVM)
## For Regression (SVR)

### Perspective on SVM regression as linear regression
> Constraint from SVC has changed(>=1 to <= epsilon)  
> By this we need to check if it is under the margin of decision boundary or above  
> We need two slack valiables (SVC: n parameters / SVR: 2n parameters)  

<img width="1120" alt="image" src="https://github.com/user-attachments/assets/90e91b6b-d23a-4ece-b5c3-278f88e827b9">  

Cost function of MSE changed to ε-insensitive loss function which only penaltize when it is out of the bound of ε.

<img width="796" alt="image" src="https://github.com/user-attachments/assets/54ebfdba-ce2f-4074-8968-2922cee507a6">  

- Either α, β is 0  
- Data above the bound of ε : -
- Data below the bound of ε : +
- Hyperparameter
    - C
    - Epsilon (High ~ underfitting)
    - kernel (nonlinear)
    - gamma(if 'rbf' kernel)
    <img width="795" alt="image" src="https://github.com/user-attachments/assets/19364dfe-83e0-40df-8455-4ae4a1f79839">


- For regression, **scaling for target values** are valid. (Slack variable depends on target value)
<img width="565" alt="image" src="https://github.com/user-attachments/assets/f79195fb-00f1-46a8-853b-1cd259766fb0">


- Strengths of SVM
    - Perform well on variety
    - Complex decision boundaries even with few features
- Weaknesses of SVM
    - Poor scalability
    - Careful on tuning of hyperparameters
    - Hard to understand(inevitable on complex models)