## Unsupervised Learning: Clustering

> Clustering is the task of partitioning the dataset into groups, called clusters.  

- Intra-cluster distances are minimized  
- Inter-cluster distances are maximized  
- Data may not have definitve "real" clusters, meaning that we group data points into same cluster that are close but the data might not have a real cluster  
- Clustering is an exploratory tool, and is useful only when it produces meaningful clusters  

### K-Means Clustering

> K-Means clustering finds k cluster centers that are representative of certain regions of the data based on an expectation-maximization procedure.  

- Strengths
    - Easy to understand and implement
    - Scalable
- Weaknesses
    - Relies on a random initialization  
    - Requires to specify the number of clusters you are looking for  
    - Highly depends on feature scaling  
    - Relatively restrictive assumptions are made on the shape of clusters.

**Goal: Assign k cluster center that represents the data**

1. Assign initial cluster centers(Random Initialization effects the result -  recommended to run the algorithm multiple times)  
2. (E-step) Assign each data point to the cluster centers
3. (M-step) Setting each cluster center as the mean of the data points that are assigned to it, repeat E-step

<img width="500" alt="image" src="https://github.com/user-attachments/assets/ba975ac5-1788-4ced-b7f1-815c4f2a0f5e">

#### Distance Metric
> Definition of close data is defaultly Euclidean distance. As we know that distance between data point are affected by feature scaling.  
> Feature scaling not always improve evaluation score.  
> For class labels, one-hot encoding is needed.   

#### Hyperparameter k
> Number of k is subjective. No definitive number exist. So we need a clustering evaluation indicator.  

#### ARI(Adjusted Random Index)
> Given the knowledge of the **ground truth class assignments labels_true** and our clustering 
algorithm assignments of the same data points labels_pred, the adjusted Rand index is a function that measures the similarity of the two assignments 

- Score between -1.0 and 1.0.
- Random labelings have an ARI close to 0.0.
- 1.0 stands for perfect match.



