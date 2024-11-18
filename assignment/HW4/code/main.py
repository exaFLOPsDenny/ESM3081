from ucimlrepo import fetch_ucirepo 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# fetch dataset 
abalone = fetch_ucirepo(id=1) 
  
# data (as pandas dataframes) 
X = abalone.data.features 
y = abalone.data.targets 

# Create subplots
num_features = X.shape[1]
fig, axes = plt.subplots(nrows=(num_features + 3) // 4, ncols=4, figsize=(24, 16))
axes = axes.flatten()

for idx, column in enumerate(X.columns):
    axes[idx].scatter(X[column], y, alpha=0.5)
    axes[idx].set_title(f"{column} vs y")
    axes[idx].set_xlabel(column)
    axes[idx].set_ylabel('y')
    axes[idx].legend(loc='best', fontsize=8)

# Remove unused subplots if the number of features isn't a multiple of 4
for ax in axes[num_features:]:
    fig.delaxes(ax)

plt.tight_layout(pad=3)
plt.show()

print(len(X))
print(num_features)

