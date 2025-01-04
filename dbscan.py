import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score, davies_bouldin_score
import warnings
warnings.filterwarnings("ignore")

# Load the CSV file
file_path = 'path'  # Path to your file
data = pd.read_csv(file_path)

# Select only the numeric columns
numeric_data = data.select_dtypes(include=[np.number])

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)

# Apply the DBSCAN algorithm
dbscan = DBSCAN(eps=0.5, min_samples=5)  # You can adjust eps and min_samples values as needed
clusters = dbscan.fit_predict(scaled_data)

# Add the results to the dataset
data['Cluster'] = clusters

# Save the clustered data to a CSV file
output_file_path = 'path' # Specify the path where the clustered data will be saved
data.to_csv(output_file_path, index=False)
print(f"Clustered data saved to: {output_file_path}")

# Calculate the number of clusters (excluding noise points)
num_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)  # Exclude noise (-1)
noise_points = list(clusters).count(-1)

# Calculate Silhouette Score and Davies-Bouldin Index
# We need to exclude the noise points for these metrics
valid_points = clusters != -1
silhouette = silhouette_score(scaled_data[valid_points], clusters[valid_points]) if valid_points.any() else None
db_index = davies_bouldin_score(scaled_data[valid_points], clusters[valid_points]) if valid_points.any() else None

# Display the results
print(f"Number of clusters (excluding noise): {num_clusters}")
print(f"Number of noise points: {noise_points}")
print(f"Silhouette Score: {silhouette:.3f}" if silhouette is not None else "Silhouette Score: Not available")
print(f"Davies-Bouldin Index: {db_index:.3f}" if db_index is not None else "Davies-Bouldin Index: Not available")

# Visualize the DBSCAN clustering
plt.figure(figsize=(12, 8))  # Increased figure size
sns.scatterplot(
    x=numeric_data.iloc[:, 0],  # X-axis is the first numeric column
    y=numeric_data.iloc[:, 1],  # Y-axis is the second numeric column
    hue=data['Cluster'],  # Color the points based on their cluster
    palette='viridis',  # Use the 'viridis' color palette
    s=150,  # Increase the point size
    legend="full",  # Show the legend
    alpha=0.9  # Decrease transparency to make points more solid
)
plt.title("DBSCAN Clustering")  # Title of the plot
plt.xlabel(numeric_data.columns[0])  # Label for X-axis
plt.ylabel(numeric_data.columns[1])  # Label for Y-axis
plt.grid(True, linewidth=0.7, color='lightgray')  # Make grid lines more visible
plt.show()  # Display the plot

# Visualize the performance metrics
metrics = ["Silhouette Score", "Davies-Bouldin Index"]
values = [silhouette if silhouette else 0, db_index if db_index else 0]

plt.figure(figsize=(8, 6))
plt.bar(metrics, values, color=["skyblue", "salmon"], alpha=0.8)
plt.title("DBSCAN Performance Metrics", fontsize=14)
plt.ylabel("Score", fontsize=12)
plt.ylim(0, 1)  # Adjust as needed
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

