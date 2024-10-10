## Linear Models

### Linear Regression
$$ \hat{y} = w^\top x + b $$
$$ when \ \ x_i = \{ 1,\ x_{i1},\ x_{i2},... \} $$
$$ \hat{y} = w^\top x $$

> Finds the parameters **w** and b that minimize the MSE between predictions and true target values  
> Has no hyperparameters, thus **no way to control model complexity**

#### Loss function  
<img width="493" alt="image" src="https://github.com/user-attachments/assets/cbae528b-523b-40c2-a57e-d22294eaf505"> <img width="285" alt="image" src="https://github.com/user-attachments/assets/f1d7ad61-f3e8-426a-9ee6-bfb0dfa17b63">

- Not only MSE can be the loss function.
 
<img width="693" alt="image" src="https://github.com/user-attachments/assets/2fedb6da-202a-4443-adb8-5a982f1ee23f">  

As there is no way to control model complexity, so want to keep the magnitude of the model parameters as small as possible.

#### Regularized Linear Regression
<img width="693" alt="image" src="https://github.com/user-attachments/assets/815efe6c-4e4f-4332-a901-d73aab56010f">

> Hyperparameter α controls how much you want to regularize  
> As Lasso regularization affects stronger, then the # of feature that are used decrease.(Not getting closer to 0 but just **'0'!!** like feature selection.)

### Logistic Regression

- Decision boundary $w^\top x + b=0$ is linear.