## Support Vector Machines (SVM)

### For Classification
> Find the hyperplane that maximizes the margin 
<img width="702" alt="image" src="https://github.com/user-attachments/assets/47956d56-dbb8-4855-8bfd-99a90d18d6ec"> <img width="295" alt="image" src="https://github.com/user-attachments/assets/ca1052fd-9e83-45f1-a181-ca38b4fe40da">

#### Hard-margin formulation
<img width="679" alt="image" src="https://github.com/user-attachments/assets/b8423975-4a1b-48f5-a89d-e68506c28bc0">

- Maximizing the margin:  
    <=> Max 2 / |w|  
    <=> Min (1/2) * w^T * w  

#### Soft-margin formulation (when data are linearly inseparable)
<img width="733" alt="image" src="https://github.com/user-attachments/assets/c49f1dca-c4c4-4dc1-8c5e-c648de064624">

- Hyperparameter C gets bigger, more 