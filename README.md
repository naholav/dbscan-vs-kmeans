Clustering Algorithms Comparison: K-Means and DBSCAN

This repository demonstrates clustering algorithms, including K-Means (both standardized and non-standardized) and DBSCAN, on a dataset. Performance metrics such as Silhouette Score and Davies-Bouldin Index are visualized and compared.

Repository Structure

1. Python Scripts
non-standardize_k-means.py: Applies K-Means clustering without standardizing the data.
standardize_k-means.py: Applies K-Means clustering with standardized data.
dbscan.py: Implements DBSCAN clustering.
2. Image Folder
Contains all visualization results, including:

dbscan.png: Scatter plot visualization for DBSCAN clustering.
k-means_non-standardized.png: Scatter plot for non-standardized K-Means clustering.
k-means_standardize.png: Scatter plot for standardized K-Means clustering.
non-standardize_k-means_vs_dbscan.png: Performance metrics comparison between non-standardized K-Means and DBSCAN.
non-standardize_vs_standardize.png: Performance comparison of non-standardized vs standardized K-Means.
standardize_k-means_vs_dbscan.png: Performance metrics comparison between standardized K-Means and DBSCAN.
3. Data Folder
Includes the following files:

non-standardize_k-means_clustered_data.csv: Clustered results for non-standardized K-Means.
standardize_k-means_clustered_data.csv: Clustered results for standardized K-Means.
dbscan_clustered_data.csv: Clustered results for DBSCAN.
pricerunner_aggregate 2.csv: Original dataset used for clustering.
How to Use

Prerequisites
Make sure the following Python libraries are installed:

numpy
pandas
matplotlib
seaborn
sklearn
Install the requirements using:

pip install numpy pandas matplotlib seaborn scikit-learn
Running the Scripts
Set File Paths
Update the following variables in each script before running:
file_path: Path to the input CSV file (e.g., pricerunner_aggregate 2.csv).
output_file_path: Path where the clustered results will be saved.
Example:

file_path = 'data/pricerunner_aggregate 2.csv'  # Input file
output_file_path = 'data/standardize_k-means_clustered_data.csv'  # Output file
Run the Scripts
Execute any of the Python scripts to generate clustered results and visualizations:
python non-standardize_k-means.py
python standardize_k-means.py
python dbscan.py
View Results
Clustered data will be saved in the data folder, and visualizations will be stored in the images folder.
Performance Comparison

This project evaluates clustering algorithms using the following metrics:

Silhouette Score: Measures how similar an object is to its own cluster compared to other clusters.
Davies-Bouldin Index: Evaluates the average similarity ratio between each cluster and its most similar cluster. Lower values indicate better clustering.
Performance comparisons are visualized in the images folder.
