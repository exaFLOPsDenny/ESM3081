## Unsupervised Learning: Dimensionality Reduction & Visualization

- The Curse of Dimensionality
    - High-dim dataset are at risk of being sparse  
    - Increase the size of training set of Dimension reduction  

- Data visualization  
    - As we are capable to visualize up to 3-dim, Dimension Reduction is needed.  

- Manifold Learning
    - It aims on visualization, rarely used if the final goal is supervised learning. Usually for unsupervised learning.

### (Manifold Learning) t-distributed Stochastic Neighbor Embedding (t-SNE)

> t-Distribution Stochasitc Neighbor Embedding(t-SNE) tries to find a low-dim representation of data that preserves the distance between points as possible.  

- points that are close in original space closer(more emphasis)  
- points that are far apart, farther apart 
- No transformation mapping exist for new data

**Goal: Find r-dim representation that best preserves the distance between points (r <> d)**  

1. Compute pairwise similarity p_ij for original data points in the training dataset D
2. Initialize r-dim representation Z^(0) by sampling from N(0,εI)
3. Update the representative(step t)
    1. Compute pairwise similarity q_ij for Z^(t-1)
    2. Compute gradient of KL(P||Q) w.r.t z
    3. <img width="500" alt="image" src="https://github.com/user-attachments/assets/397c2481-04a4-4ddd-b953-548fe3f41002">

<img width="500" alt="image" src="https://github.com/user-attachments/assets/c0092c0e-46f9-4066-be8f-bddacc73a1d5">  

<img width="500" alt="image" src="https://github.com/user-attachments/assets/f51f5120-b618-4ee4-b87f-a6f29943b4d9">