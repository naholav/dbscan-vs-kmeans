import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score
import matplotlib.pyplot as plt
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")


def load_data(file_path):
    """Loads the dataset."""
    return pd.read_csv(file_path)


def perform_kmeans(data, n_clusters=3, n_init=30, max_iter=1000):
    """Performs K-Means clustering."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=n_init, max_iter=max_iter)
    kmeans.fit(data)
    return kmeans


def evaluate_clustering(data, labels):
    """Evaluates clustering performance."""
    silhouette_avg = silhouette_score(data, labels)
    davies_bouldin = davies_bouldin_score(data, labels)
    return silhouette_avg, davies_bouldin


def visualize_clusters(data, cluster_labels, title="K-Means Clustering"):
    """Visualizes clusters with a scatter plot."""
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(
        data['Product ID'], data['Merchant ID'], c=cluster_labels, cmap="viridis", alpha=0.7, s=30
    )
    plt.colorbar(scatter, label="Cluster")
    plt.title(title)
    plt.xlabel("Product ID")
    plt.ylabel("Merchant ID")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()


def visualize_metrics(silhouette, davies_bouldin):
    """Visualizes Silhouette Score and Davies-Bouldin Index."""
    metrics = ["Silhouette Score", "Davies-Bouldin Index"]
    values = [silhouette, davies_bouldin]

    plt.figure(figsize=(8, 6))
    plt.bar(metrics, values, color=["skyblue", "salmon"], alpha=0.8)
    plt.title("K-Means Clustering Performance Metrics", fontsize=14)
    plt.ylabel("Score", fontsize=12)
    plt.ylim(0, 1)  # Adjust as needed
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()


# 1. Load Data
file_path = 'path' # Path to your file
data = load_data(file_path)

# 2. Clean column names (if necessary)
data.columns = data.columns.str.strip()  # Removes leading/trailing spaces
data.columns = data.columns.str.replace(r'[^\w\s]', '', regex=True)  # Removes special characters

# 3. Ensure required columns exist
if 'Product ID' not in data.columns or 'Merchant ID' not in data.columns:
    raise KeyError("Dataset must contain 'Product ID' and 'Merchant ID' columns.")

# 4. Select features for clustering
features = data[['Product ID', 'Merchant ID']]

# 5. Perform K-Means Clustering
optimal_clusters = 3  # Adjust the number of clusters as needed
kmeans = perform_kmeans(features, n_clusters=optimal_clusters)
features.loc[:, 'Cluster'] = kmeans.labels_  # Add cluster labels for visualization

# 6. Evaluate Clustering Performance
silhouette_avg, davies_bouldin = evaluate_clustering(features, kmeans.labels_)
print(f"K-Means Silhouette Score: {silhouette_avg:.4f}")
print(f"K-Means Davies-Bouldin Index: {davies_bouldin:.4f}")

# 7. Visualize Clusters
visualize_clusters(features, kmeans.labels_, title="K-Means Clustering on Product and Merchant ID")

# 8. Visualize Performance Metrics
visualize_metrics(silhouette_avg, davies_bouldin)

# 9. Save Results
save_path = 'path' # Specify the path where the clustered data will be saved
features.to_csv(save_path, index=False)
print(f"Clustering results saved to: {save_path}")

