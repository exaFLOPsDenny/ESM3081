import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.metrics import adjusted_rand_score
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Flags to toggle PCA and Feature Selection
use_pca = True
use_feature_selection = False

# Load the Abalone dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
column_names = ["Sex", "Length", "Diameter", "Height", "WholeWeight", "ShuckedWeight", "VisceraWeight", "ShellWeight", "Rings"]
data = pd.read_csv(url, header=None, names=column_names)

# Encode 'Sex' as numeric
data['Sex'] = data['Sex'].map({'M': 0, 'F': 1, 'I': 2})

# Case 1: 4-7

# Bin Rings (Binning from 1-4, 5-9, 10-14, etc.)
bins = [0, 4, 8, 12, 16, 20, 24, 29]
labels = [0, 1, 2, 3, 4, 5, 6]
data['RingBin'] = pd.cut(data['Rings'], bins=bins, labels=labels, include_lowest=True)

# Separate features and labels
X = data.drop(columns=['Rings', 'RingBin'])
y = data['RingBin']
y_real = data["Rings"]

# Standardize features
# scaler = MinMaxScaler --> Standard is better!

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Feature Selection
if use_feature_selection:
    selector = SelectKBest(score_func=f_classif, k=6)
    X_processed = selector.fit_transform(X_scaled, y)
    print(f"Feature selection reduced the number of features to {X_processed.shape[1]}.")
else:
    X_processed = X_scaled

# PCA for Dimensionality Reduction
if use_pca:
    pca = PCA(n_components=0.95, random_state=42)
    X_processed = pca.fit_transform(X_processed)
    print(f"PCA reduced the number of features to {X_processed.shape[1]}.")
else:
    print("PCA skipped.")

# Step 1: Perform K-Means clustering with 7 clusters (global clustering)
kmeans_7 = KMeans(n_clusters=7, n_init=100, random_state=42)
data['Cluster_label'] = kmeans_7.fit_predict(X_processed)

# Step 2: Perform K-Means clustering within each bin (local clustering
for bin_label in labels:
    bin_data = data[data['Cluster_label'] == bin_label]
    if not bin_data.empty:
        kmeans_bin = KMeans(n_clusters=4, random_state=42)
        bin_clusters = kmeans_bin.fit_predict(X_processed[bin_data.index])
        cluster_label = [f"{bin_label}_{cluster}" for cluster in bin_clusters]
        data.loc[bin_data.index,"Cluster_label" ] = cluster_label
          

# Map 'Cluster_label' to numeric values for t-SNE and ARI computation
data['Cluster_numeric'] = data['Cluster_label'].astype('category').cat.codes

# Extract features (all columns except 'Cluster_label' and 'Cluster_numeric')
features = data.drop(columns=['Cluster_label', 'Cluster_numeric']).values
cluster_labels = data['Cluster_numeric'].values

# Apply t-SNE for visualization
tsne = TSNE(n_components=2, random_state=42)
tsne_results = tsne.fit_transform(features)

# Plot t-SNE results
plt.figure(figsize=(10, 7))
scatter = plt.scatter(tsne_results[:, 0], tsne_results[:, 1], c=cluster_labels, cmap='tab20', s=30, alpha=0.7)
plt.colorbar(scatter, label='Cluster Label')
plt.title('t-SNE Visualization of Clusters', fontsize=14)
plt.xlabel('t-SNE Dimension 1', fontsize=12)
plt.ylabel('t-SNE Dimension 2', fontsize=12)
plt.show()

# Compute ARI score
ari_score = adjusted_rand_score(y_real, cluster_labels)
print(f"Adjusted Rand Index (ARI): {ari_score:.4f}")
