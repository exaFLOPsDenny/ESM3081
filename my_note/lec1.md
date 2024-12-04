## Learning

> Generalizing training dataset to build a prediction model for unknown test data  
> Prediction model is a functional relationship between X and y  

## Supervised
 
> Training dataset with labels  
- Type   
    - Classification (class label- discrete)  
    - Regression (continuity label)  
    
## Generalization
> Accurate for unknown data 

- Type of failure  
    - Overfitting  
        > Model too complex for the amount of data  
        > Model fit too closely to the particularities of the training set  
        > Work well on training set, but not on test set  
    - Underfitting  
        > Model too simple for the amount of data  
        > Model fails to capture all the aspects of and variability in the training set  
        > Work badly even on the training set  


Relevance between generalization failure and model complexity  
> Larger variety of data points(more data you collect) more complex model you can use without overfitting  
> Tradeoff between accuracy and model complexity  

<img width="336" alt="image" src="https://github.com/user-attachments/assets/7e965d59-2cef-4bb4-be45-58fbe3fc3076">

## Model Parameters / Hyperparameters
Parameter  
> Configuration internal to the model  
> derived via model training

Hyperparmeters
> Configuration for training of the model  
> Set before model training

## Dataset

Training set  
> to learn the **parameters** of the model

Validation set  
> to choose the **hyperparameters** of the model  

Test set  
> for final evaluation of the **generalizaiton ability** of the model

## Performance Evalutation

