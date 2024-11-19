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