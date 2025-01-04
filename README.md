# **K-Means and DBSCAN Clustering Performance Analysis**

This repository contains Python implementations for clustering analysis using **K-Means** and **DBSCAN** algorithms. It demonstrates the effects of data standardization on clustering performance and provides visual and statistical insights into the results.

---

## **Project Goals**

The primary goals of this project are:
1. **Clustering Algorithm Comparison**:
   - Evaluate the performance of **K-Means** and **DBSCAN** algorithms on a dataset.
2. **Impact of Standardization**:
   - Investigate how data standardization influences clustering outcomes.
3. **Performance Metrics**:
   - Analyze clustering performance using **Silhouette Score** and **Davies-Bouldin Index**.
4. **Visualization**:
   - Provide clear and informative visualizations of clustering results.

---

## **Repository Structure**
project_directory/ ├── data/ │ ├── pricerunner_aggregate 2.csv │ ├── non-standardize_k-means_clustered_data.csv │ ├── standardize_k-means_clustered_data.csv │ ├── dbscan_clustered_data.csv ├── images/ │ ├── k-means_non-standardized.png │ ├── k-means_standardize.png │ ├── dbscan.png │ ├── non-standardize_k-means_vs_dbscan.png │ ├── non-standardize_vs_standardize.png │ ├── standardize_k-means_vs_dbscan.png ├── non-standardize_k-means.py ├── standardize_k-means.py ├── dbscan.py ├── requirements.txt └── README.md


---

## **Datasets**

### **1. `pricerunner_aggregate 2.csv`**
- Contains information about products and merchants used for clustering.
- Key columns:
  - `Product ID`
  - `Merchant ID`

### **2. Clustered Data Outputs**
- **`non-standardize_k-means_clustered_data.csv`**: Results of K-Means clustering without standardization.
- **`standardize_k-means_clustered_data.csv`**: Results of K-Means clustering with standardization.
- **`dbscan_clustered_data.csv`**: Results of DBSCAN clustering.

---

## **Python Scripts**

### **1. `non-standardize_k-means.py`**
- Implements K-Means clustering without standardizing the data.
- Outputs clustering performance metrics and visualizations.

### **2. `standardize_k-means.py`**
- Implements K-Means clustering with standardized data.
- Highlights the improvement in clustering performance after standardization.

### **3. `dbscan.py`**
- Applies the DBSCAN clustering algorithm.
- Includes performance metrics for non-standardized data.

---

## **Performance Metrics**

### **Silhouette Score**
- Measures how similar an object is to its cluster compared to other clusters.
- Range: `-1` (poor clustering) to `1` (ideal clustering).

### **Davies-Bouldin Index**
- Evaluates the compactness and separation of clusters.
- Lower values indicate better clustering.

---

## **Visualizations**

### Key Visualizations:
1. **K-Means vs DBSCAN Performance (Non-Standardized)**:
   ![Non-Standardized K-Means vs DBSCAN](images/non-standardize_k-means_vs_dbscan.png)

2. **Impact of Standardization on K-Means**:
   ![Standardized vs Non-Standardized K-Means](images/non-standardize_vs_standardize.png)

3. **K-Means vs DBSCAN Performance (Standardized)**:
   ![Standardized K-Means vs DBSCAN](images/standardize_k-means_vs_dbscan.png)

---

## **Installation**

1. Clone this repository:
   ```bash
   git clone https://github.com/<your_username>/<repository_name>.git
   cd <repository_name>
2. Install dependencies:
   '''bash
   pip install -r requirements.txt
   
