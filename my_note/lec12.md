## Model Evaluation and Improvement
### Evaluation metrics and Scoring

- Business metric: high level goal of application
- Surrogate evaluation procedure: the closest metric to the business metric that is feasible to evaluate

#### Binary Classification
- Confusion Matrix
<img width="700" alt="image" src="https://github.com/user-attachments/assets/a7c170b0-e572-455b-bab9-f0864cdc9e45">

- Error
    - Type 1 Error: FP, usually more important
    - Type 2 Error: FN

- Accuarcy
    - Same weight between FP & FN, inappropriate for imbalanced dataset

- Tradeoff between recall and precision
    - More positive prediction, higher recall, but lower precision
    - F1 score: harmonic mean of precision and recall

- Tradeoff between Sensitivity(Recall) and Specificity
    - Balanced Accuracy: arithmetic mean of sensitivity and specificity

- Uncertainty
    - decision_function threshold: -0.8 -> more positives
    - predict_proba: 0.75 -> more negatives
    <img width="700" alt="image" src="https://github.com/user-attachments/assets/82d589bc-27d5-4317-b8cc-9a513516b0bd">


#### Multi-Class Classification
<img width="700" alt="image" src="https://github.com/user-attachments/assets/e8feb4c1-4ef0-45dd-b13a-c32897a01c6a">

- Multiclass version of the F1 score
    - Micro Averaging
        - computes the total number of false positives, false negatives, and true positives over all classes, and then computes precision, recall, and F1-score using these couunt
        - Precision and Recall is the same
        - Equivalent to conventional classification accuracy counts
        - Focus on each data point equally(majority on class is affected)
    
    - Weighted Averaging
        - computes the weighted mean of the per-class F1-scores, weighted by their support

    - Macro Averaging
        - computes the unweighted mean of the per-class F1-scores, giving equal weight to all classes
        - Usually smaller than micro F1 score under class imbalance
        - Focus on each class equally
<img width="700" alt="image" src="https://github.com/user-attachments/assets/08c73819-4823-416f-9dbb-30f8f129cfa0">

#### Regression

- Interval Scale (e.g. temperature)
    - no absolute zero
    - difference between magnitudes
    - MAPE : no true value for 0 
- Ratio Scale
    - abosolute zero
    - difference between magnitudes
    - ration between magnitudes

<img width="500" alt="image" src="https://github.com/user-attachments/assets/5ffe5e22-87ed-4ea9-bf84-8f85d3638edc">

<img width="700" alt="image" src="https://github.com/user-attachments/assets/d4a86ef3-10f9-4668-946d-444b1e534620">

- More penalty on large errors
    - RMSE
- Interval Scale(차이가 2배야 어색)
    - MAPE
- Ratio Scale
    - MAE
- RMSE and R^2 are alike

### Cross-Validation
<img width="700" alt="image" src="https://github.com/user-attachments/assets/2b08550b-f6d1-4aff-9da3-4feebded8729">

> The goal of splitting data: Generalized model to unseen data  
> Results depend on a particular random choice for the partition  

- Cross-Validation
    - All data points be in test dataset **once**
    - Data are split repeatedly and multiple models are trained
    - Computation cost is increased but we usually use Cross-validation on small dataset so not such a big deal

- k-Fold Cross-Validation
<img width="700" alt="image" src="https://github.com/user-attachments/assets/ac0b9fcc-0440-46be-939a-c15c28bacc40">

- Stratified k-Fold Cross-Validation
<img width="700" alt="image" src="https://github.com/user-attachments/assets/2ae38dc6-c274-4696-9703-4b5196a9565e">

- Leave-one-out Cross-Validation
<img width="700" alt="image" src="https://github.com/user-attachments/assets/9d2346c5-181a-4911-80a0-61da65dc27f1">

### Grid Search
> Trying all possible combinations of the hyperparameters of interest 

- Computationally expensive, so start with small grid

- Grid search with Cross-Validation
    - Effective for small datasets
    - Rebuild a model with best hyperparameter
    - ensemble of the k models (hard voting, soft voting)
<img width="700" alt="image" src="https://github.com/user-attachments/assets/9be7989d-dac4-4bbc-9135-436c31f5008e">

- Grid search with Nested Cross-Validation
<img width="700" alt="image" src="https://github.com/user-attachments/assets/494c8409-4a4f-413f-bc3b-2fbe7f3ecf3b">

- Advanced method (not Grid search)
    - Random search
    - Meta-heuristcs
    - Model-based Optimization

**Should not test different hyperparameter ranges on the final test set or repeat testing with differenct models more than once**