# **Clustering and Data Analysis**

This repository contains a project that focuses on clustering and analyzing a dataset using various clustering algorithms such as K-Means and DBSCAN. The project also includes visualizations and performance metrics to compare the effectiveness of these algorithms.

---

## **Project Overview**

The project provides implementations of two clustering algorithms:
1. **K-Means**: Both standardized and non-standardized versions.
2. **DBSCAN**: Density-Based Spatial Clustering of Applications with Noise.

The repository contains Python scripts, sample datasets, and visualizations to analyze and understand the clustering results.

---

## **Folder Structure**

project/ ├── data/ │ ├── pricerunner_aggregate_2.csv │ ├── non-standardize_k-means_clustered_data.csv │ ├── standardize_k-means_clustered_data.csv │ ├── dbscan_clustered_data.csv ├── images/ │ ├── k-means_non-standardized.png │ ├── k-means_standardize.png │ ├── dbscan.png │ ├── non-standardize_k-means_vs_dbscan.png │ ├── non-standardize_vs_standardize.png │ ├── standardize_k-means_vs_dbscan.png ├── non-standardize_k-means.py ├── standardize_k-means.py ├── dbscan.py ├── requirements.txt ├── README.md


---

## **Requirements**

To run this project, you need the following Python libraries:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

All dependencies are listed in the `requirements.txt` file.

---

## **How to Install Dependencies**

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project/
Install dependencies using the requirements.txt file:
pip install -r requirements.txt
Python Scripts

1. non-standardize_k-means.py
Implements the K-Means clustering algorithm without standardizing the data.
Outputs the clustering results and performance metrics (Silhouette Score and Davies-Bouldin Index).
Saves the clustered data as non-standardize_k-means_clustered_data.csv.
2. standardize_k-means.py
Implements the K-Means clustering algorithm with standardized data.
Outputs the clustering results and performance metrics (Silhouette Score and Davies-Bouldin Index).
Saves the clustered data as standardize_k-means_clustered_data.csv.
3. dbscan.py
Implements the DBSCAN clustering algorithm.
Outputs the clustering results and performance metrics (Silhouette Score and Davies-Bouldin Index).
Saves the clustered data as dbscan_clustered_data.csv.
Datasets

The data/ folder contains the following files:

pricerunner_aggregate_2.csv: The original dataset used for clustering.
non-standardize_k-means_clustered_data.csv: Clustered data from the non-standardized K-Means algorithm.
standardize_k-means_clustered_data.csv: Clustered data from the standardized K-Means algorithm.
dbscan_clustered_data.csv: Clustered data from the DBSCAN algorithm.
Visualizations

The images/ folder contains visualizations comparing the clustering results:

k-means_non-standardized.png: Results of non-standardized K-Means clustering.
k-means_standardize.png: Results of standardized K-Means clustering.
dbscan.png: Results of DBSCAN clustering.
non-standardize_k-means_vs_dbscan.png: Comparison of non-standardized K-Means and DBSCAN.
non-standardize_vs_standardize.png: Comparison of non-standardized and standardized K-Means.
standardize_k-means_vs_dbscan.png: Comparison of standardized K-Means and DBSCAN.
How to Run the Scripts

Run non-standardize K-Means:
python non-standardize_k-means.py
Modify file_path in the script to point to the dataset location.
Modify output_file_path to specify the save location for clustered data.
Run standardize K-Means:
python standardize_k-means.py
Modify file_path in the script to point to the dataset location.
Modify output_file_path to specify the save location for clustered data.
Run DBSCAN:
python dbscan.py
Modify file_path in the script to point to the dataset location.
Modify output_file_path to specify the save location for clustered data.
Key Insights

K-Means Clustering
Standardizing the data before applying K-Means improved clustering performance, as indicated by better Silhouette Scores and lower Davies-Bouldin Index values.
Visualizations highlight clear differences in cluster separability between standardized and non-standardized data.
DBSCAN Clustering
DBSCAN effectively identifies noise points and clusters based on density.
Requires careful tuning of eps and min_samples for optimal results.
Compared to K-Means, DBSCAN is more robust to outliers but may struggle with high-dimensional data.
Algorithm Comparison
K-Means:
Performs well with spherical clusters.
Sensitive to scaling and outliers.
DBSCAN:
Excels in identifying arbitrary-shaped clusters.
Robust to outliers but parameter-sensitive.
Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any bug fixes, enhancements, or additional features.
