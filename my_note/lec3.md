## Linear Models
> Linear combination of features and parameters

- Strengths
    - Linear models are very fast to train and to predict (Inner production with features and parameters)
    - scale to very large dataset and work well with sparse data
    - easy to understand
- Weekness
    - Highly correlated features can fuzz the meaning of the coefficient
    - relationship between feature and target should be linear


### Linear Regression
$$ \hat{y} = w^\top x + b $$
$$ when \ \ x_i = \{ 1,\ x_{i1},\ x_{i2},... \} $$
$$ \hat{y} = w^\top x $$

> Finds the parameters **w** and b that minimize the MSE between predictions and true target values  
> Has no hyperparameters, thus **no way to control model complexity**

### Loss function  
<img width="493" alt="image" src="https://github.com/user-attachments/assets/cbae528b-523b-40c2-a57e-d22294eaf505"> <img width="285" alt="image" src="https://github.com/user-attachments/assets/f1d7ad61-f3e8-426a-9ee6-bfb0dfa17b63">

- Not only MSE can be the loss function.
 
<img width="693" alt="image" src="https://github.com/user-attachments/assets/2fedb6da-202a-4443-adb8-5a982f1ee23f">  

As there is no way to control model complexity, so want to keep the magnitude of the model parameters as small as possible.

### Regularized Linear Regression
<img width="693" alt="image" src="https://github.com/user-attachments/assets/815efe6c-4e4f-4332-a901-d73aab56010f">

- Hyperparameter α controls how much you want to regularize  
- In scikit-learn, L2 is default and as the c(hyperparmeter) gets bigger the less of it's affectiveness, as c is the "inverse of regularization strenght"  
- As Lasso regularization affects stronger, then the # of feature that are used decrease.(Not getting closer to 0 but just **'0'!!** like feature selection.)


<details>
<summary> Where to use L1 regularization or L2 regularization?</summary>
L1 - feature selection(large amount of features and assume that only a few of them are actually important) <br>
L2 - closed-form possible unlike L1 have to find numerical solution
</details>

### Logistic Regression

<img width="763" alt="image" src="https://github.com/user-attachments/assets/8cc9c956-e9b8-48e5-ba67-447bca29c543">

- Decision boundary $w^\top x + b=0$ is linear.
- No deterministic solution for Logistic Regression exist
<img width="687" alt="image" src="https://github.com/user-attachments/assets/cf43c62a-34a3-419a-a38f-aaa5db55ded2">

- Cross-entropy aligns with probabilist interpretation with Bernoulli distribution

### Gradient Descent(for no closed-form solution)

<img width="654" alt="image" src="https://github.com/user-attachments/assets/db48f668-5df5-4476-89f3-3be204d8d40a">

- If the learning-rate is not closed to 0, the assumption of First-order approximation is crushed.

<img width="750" alt="image" src="https://github.com/user-attachments/assets/80f13f76-ab42-4395-8a84-2ddc1657214f">
