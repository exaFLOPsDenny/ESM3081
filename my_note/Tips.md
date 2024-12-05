1. MSE's deterministic solution induction
2. Not only MSE but other loss function can be used
3. Where did GD come from? And why lr should be close to 0?
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
    - RF (Boostrap 0: generalized / max_feature: high ~ overfitting)
    - SVC (C: big ~ overfitting)
    - SVR (C: big ~ overfitting/ epsilon: small ~ overfitting / gamma in rbf kernel: big ~ overfitting)
    - NN (complex hidden layer ~ overfitting)
12. learning rate should be small if not the assumption of taylor expansion fails
13. No free lunch 절대적으로 낫다 는 없다
14. DT는 비교적 feature scaling에 영향을 덜 받는다(0~1 보단 -1~1까지 0을 중심으로 하는 것이 더 좋다)
<img width="861" alt="image" src="https://github.com/user-attachments/assets/0b576612-fb2e-43eb-af03-7a82501e702b">

15. Big data 에 좋은 것: Linear model, NN
16. Big data 에 안 좋은 것: SVM, KNN
17. Regularization이 어느 수준 이상으로 과도하게 강하면 모든 파라미터가 0에 수렴하면서 모든 예측을 0으로 하게 됩니다.
18. Linear regression 사용 시 training R^2은 0부터 1 사이의 값을 가지게 되나, test R^2은 음수의 값을 가질 수 있습니다.-> 단순한 평균 예측보다도 더 나쁜 성능을 보인다는 의미 (R^2의 definition을 생각해볼 것-> 잔차 제곱합이 총 제곱합보다 크면 R² 값이 음수가 될 수 있습니다.). 다른 알고리즘 사용시 이론적으로 training R^2도 0보다 작을 수도 있습니다. 그러나 어떠한 경우에도 R^2은 항상 1보다 클 수는 없습니다.
19. t-SNE class has no transform method  
<img width="500" alt="image" src="https://github.com/user-attachments/assets/cb4d6438-2907-4f03-b78e-509c82863814">

20. Hierachical Clustering-Agglomerative has no predict method, Once a decision is made to combine two clusters, it cannot be undone
21. DBSCAN also no predict method
22. If the model is Logistic regression it includes bias term - Polynomial feature engineering include_bias should be false!
23. <img width="700" alt="image" src="https://github.com/user-attachments/assets/8411a395-c0d4-4c53-a43f-f91e42f0daa9">
hyperparameter 설정 전 train과 validation 각각을 scale해주고 hyperparmeter를 찾은 뒤 train+validation을 합친 것에 대해 다시 scale
<img width="700" alt="image" src="https://github.com/user-attachments/assets/0c8a52be-ead1-4178-bd0a-d22e7ec88863">