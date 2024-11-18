### Data Preprocessing and Scaling
> New representation of the data which might be easier to understand

> Scaling is one of Pre-processing steps, but not always brings enhancement

- StandardScaler
    - mean:0 and variance:1
- MinMaxScaler
    - shift between 0~1 (default)
    - Usually feature_range=(-1,1) so that the center is 0 for stability of learning especially NN.
- RobustScaler
    - median rather than mean, interquartile rather than variance 
    - Robust on outliers   

## Unsupervised Learning
> (in general) Unlabeled training dataset  
> Goal is to find useful properties/patterns of the structures of the dataset

#### Unsupervised Learning is relatively harder than Supervised Learning with respect to understanding and evaluating. It is subjective in the sense of PATTERN they think to use as a standard.

- Rather than tuning the hyperparameters, manually evaluation is needed.  
- Rather than making large automatic system, used as exploratory setting to understand the data better.
