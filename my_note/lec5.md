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

- Introducing slack parameter  
- Hyperparameter C gets **bigger**, more focus on sum of slack variable(hinge), **less focus on regularization, occuring overfitting**
- Cost function can be seen as using slack summation instead of cross entropy and using L2 regulatization on Logistic regression
- As it is convex problem, we can use Largrange multiplier method and also guarantees global optimum  

<img width="733" alt="image" src="https://github.com/user-attachments/assets/c49f1dca-c4c4-4dc1-8c5e-c648de064624">

<img width="619" alt="image" src="https://github.com/user-attachments/assets/cc493b9a-58de-4d2a-970c-b60af74d3c05">

<img width="340" alt="image" src="https://github.com/user-attachments/assets/882974bc-1572-418d-8911-17c94f1a770c">

<img width="619" alt="image" src="https://github.com/user-attachments/assets/b4fb484b-bc71-4d58-b2e1-a1f5be7b8660">

<img width="644" alt="image" src="https://github.com/user-attachments/assets/536aff6b-69d3-4e44-8be4-5cdddfb7278a">

<img width="644" alt="image" src="https://github.com/user-attachments/assets/4e296dc2-aa92-40f0-990d-4601eed4746a">

<img width="1087" alt="image" src="https://github.com/user-attachments/assets/0398efb6-b0b9-49ed-95af-fda585ab6160">

<img width="856" alt="image" src="https://github.com/user-attachments/assets/0a34e92a-3cb7-42d3-94a7-eebb48b6d77b">


### Kernelized SVM

> Some dataset are nonlinearly seperable and can be limiting in low-dimensional input space  

<details>
<summary> Advantage using kernel</summary>
As compuation only require inner product, by defining k (kernel) without knowing what function φ which is replacing attributes into features.
But not all functions can be kernels.
</details>

<img width="839" alt="image" src="https://github.com/user-attachments/assets/78558249-2dec-48a3-bff8-2b72360a553a">

- lower value of gamma: underfitting
- higher value of gamma: overfitting
-> Grid-search for hyperparameter optimization
