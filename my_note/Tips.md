1. MSE's deterministic solution induction
2. Not only MSE but other loss function can be used
3. Where did GD come from? And why lr should be close to 0?
4. Wrong debugging will loss points
5. Non-linear activation function for hidden units, without this despite a lot of hidden layers it is still a linear model
6. Why margin 2/|w|
7. SVM에서 alpha가 0, +, - 의미
8. scaling 시에 X_train만!!!! <img width="436" alt="image" src="https://github.com/user-attachments/assets/97834108-cc3a-4340-9fae-cb0722388fd5">
regression 에서는 y값에도
9. number of parameters in SVM for classification(n) for regression(2n)
10. Logistic regression label(0,1) SVC(-1,1)
11. Hyperparameter and generalization(단순해진다-regulatization 강해진다)
    - KNN (low k ~ overfitting)
    - low regularization term alpha ~ overfitting
    - very large alpha ~ flat line foing through the mean of the labels in the training set
    - DT (max_depth: high ~ overfitting / min_sample_leaf: low ~ overfitting / max_leaf_nodes: high ~ overfitting)
    - RF (Boostrap 0: generalized / max_feature: low ~ overfitting)
     
12. learning rate should be small if not the assumption of taylor expansion fails
13. No free lunch 절대적으로 낫다 는 없다
14. DT는 비교적 feature scaling에 영향을 덜 받는다(0~1 보단 -1~1까지 0을 중심으로 하는 것이 더 좋다)
<img width="861" alt="image" src="https://github.com/user-attachments/assets/0b576612-fb2e-43eb-af03-7a82501e702b">

15. Big data 에 좋은 것: Linear model, NN
16. Big data 에 안 좋은 것: SVM, KNN
17. Regularization이 어느 수준 이상으로 과도하게 강하면 모든 파라미터가 0에 수렴하면서 모든 예측을 0으로 하게 됩니다.