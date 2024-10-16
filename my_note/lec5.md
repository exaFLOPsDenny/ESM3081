## Support Vector Machines (SVM)

### For Classification
> Find the hyperplane that maximizes the margin   

<img width="702" alt="image" src="https://github.com/user-attachments/assets/47956d56-dbb8-4855-8bfd-99a90d18d6ec"> <img width="295" alt="image" src="https://github.com/user-attachments/assets/ca1052fd-9e83-45f1-a181-ca38b4fe40da">

#### Hard-margin formulation
<img width="679" alt="image" src="https://github.com/user-attachments/assets/b8423975-4a1b-48f5-a89d-e68506c28bc0">

- Maximizing the margin:  
    <=> Max 2 / |w|  
    <=> Min (1/2) * w^T * w  
- No hyperparameter, only w and b as parameter

#### Soft-margin formulation (when data are linearly inseparable)
<img width="733" alt="image" src="https://github.com/user-attachments/assets/c49f1dca-c4c4-4dc1-8c5e-c648de064624">

- Introducing slack parameter  
- Hyperparameter C gets bigger, more focus on slack variable
- Cost function can be seen as using slack summation instead of cross entropy and using L2 regulatization on Logistic regression
- As it is convex problem, we can use Largrange multiplier method  

<img width="619" alt="image" src="https://github.com/user-attachments/assets/cc493b9a-58de-4d2a-970c-b60af74d3c05">

<img width="619" alt="image" src="https://github.com/user-attachments/assets/b4fb484b-bc71-4d58-b2e1-a1f5be7b8660">

<img width="768" alt="image" src="https://github.com/user-attachments/assets/35ee3b40-827e-4fd5-aeef-f20695e0cb4f">