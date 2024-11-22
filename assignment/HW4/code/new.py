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

# Bin Rings (Binning from 1-4, 5-9, 10-14, etc.)
bins = [0, 4, 8, 12, 16, 20, 24, 29]
labels = [0, 1, 2, 3, 4, 5, 6]
data['RingBin'] = pd.cut(data['Rings'], bins=bins, labels=labels, include_lowest=True)

# Separate features and labels
X = data.drop(columns=['Rings', 'RingBin'])
y = data['RingBin']

# Standardize features
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

# Step 1: Perform K-Means clustering with 6 clusters (global clustering)
kmeans_7 = KMeans(n_clusters=7, n_init=100, random_state=42)
data['Cluster_7'] = kmeans_7.fit_predict(X_processed)

# Step 2: Perform K-Means clustering within each bin (local clustering)
for bin_label in labels:
    bin_data = data[data['RingBin'] == bin_label]
    if not bin_data.empty:
        kmeans_bin = KMeans(n_clusters=4, random_state=42)
        bin_clusters = kmeans_bin.fit_predict(X_processed[bin_data.index])
        data.loc[bin_data.index, f'Cluster_Bin_{bin_label}'] = bin_clusters

# Combine all clusters into a final label
data['Final_Cluster'] = data['Cluster_7'].astype(str)
for bin_label in labels:
    if f'Cluster_Bin_{bin_label}' in data.columns:
        data['Final_Cluster'] += '_' + data[f'Cluster_Bin_{bin_label}'].fillna(-1).astype(int).astype(str)

# Encode Final_Cluster to numeric labels for visualization and ARI computation
label_encoder = LabelEncoder()
merged_clusters = label_encoder.fit_transform(data['Final_Cluster'])

# Step 3: Apply t-SNE on the processed features
tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
X_tsne = tsne.fit_transform(X_processed)

# Plot the t-SNE results for 28 clusters
plt.figure(figsize=(12, 8))
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=merged_clusters, cmap='tab20', s=10)
plt.title("t-SNE Visualization of 28 Merged Clusters")
plt.colorbar(label="Merged Cluster")
plt.xlabel("t-SNE Component 1")
plt.ylabel("t-SNE Component 2")
plt.show()

# Step 4: Compute ARI for Merged Clusters (Final Clusters vs RingBin)
ari_merged = adjusted_rand_score(data['RingBin'].astype(float), merged_clusters)
print(f"ARI for Merged Clustering (Final Clusters vs RingBin): {ari_merged:.4f}")

# Step 5: Optional - Plot distribution of final clusters
final_cluster_counts = pd.Series(merged_clusters).value_counts()
final_cluster_counts.plot(kind='bar', figsize=(12, 6), title="Distribution of Final Clusters")
plt.xlabel("Cluster Labels")
plt.ylabel("Number of Points")
plt.show()
