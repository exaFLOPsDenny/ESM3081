## Unsupervised Learning: Clustering

> Clustering is the task of partitioning the dataset into groups, called clusters.  

- Intra-cluster distances are minimized  
- Inter-cluster distances are maximized  
- Data may not have definitve "real" clusters, meaning that we group data points into same cluster that are close but the data might not have a real cluster  
- Clustering is an exploratory tool, and is useful only when it produces meaningful clusters  

### K-Means Clustering

> K-Means clustering finds k cluster centers that are representative of certain regions of the data based on an expectation-maximization procedure.  

**Goal: Assign k cluster center that represents the data**

1. Assign initial cluster centers
2. (E-step) Assign each data point to the cluster centers
3. (M-step) Setting each cluster center as the mean of the data points that are assigned to it, repeat E-step