# Mall Customer Segmentation using Unsupervised Machine Learning

## Project Overview

This project performs customer segmentation using three popular unsupervised machine learning algorithms:

- K-Means Clustering
- Hierarchical (Agglomerative) Clustering
- DBSCAN (Density-Based Spatial Clustering)

The goal is to identify groups of customers based on their purchasing behavior so businesses can design targeted marketing strategies and improve customer engagement. The final model is deployed as an interactive web app.

---

## Live Demo

**Try it here:** [[ https://mall-customer-segmentation-adi.streamlit.app/ ]] 

Enter a customer's Annual Income and Spending Score and the app predicts which segment they belong to, with an interactive visualization showing where they fall among existing customers.

---

## Dataset

**Dataset:** Mall Customers Dataset

**Features Used:**

- Age
- Annual Income (k$)
- Spending Score (1-100)

Target variable is not available because this is an unsupervised learning problem.

---

## Project Workflow

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Cleaning
4. Feature Selection
5. Feature Scaling
6. K-Means Clustering
7. Elbow Method
8. Cluster Visualization
9. Cluster Analysis
10. Hierarchical Clustering
11. Dendrogram Visualization
12. DBSCAN Clustering (eps selected via K-Distance Graph)
13. Comparison of Clustering Algorithms
14. Business Insights & Cluster Naming
15. Model Deployment (Streamlit)

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- SciPy
- Streamlit
- Plotly

---

## Clustering Algorithms

### K-Means Clustering

- Used the Elbow Method to determine the optimal number of clusters.
- Selected **K = 5**.
- Silhouette Score: **0.5547**

---

### Hierarchical Clustering

- Applied Agglomerative Clustering using Ward Linkage.
- Used a Dendrogram to analyze cluster formation.
- Silhouette Score: **0.5538**

---

### DBSCAN

- Parameters (`eps` selected via K-Distance Graph):
  - eps = 0.5
  - min_samples = 5

Results:

- 2 Clusters
- 8 Noise Points
- Silhouette Score (noise excluded): **0.3876**

---

## Results

### Elbow Method

The Elbow Method was used to determine the optimal number of clusters. The optimal value of **K = 5** was selected.

![Elbow Method](images/Elbow_Method.png)

---

### K-Means Clustering

The K-Means algorithm segmented customers into five distinct groups based on Annual Income and Spending Score.

![K-Means Clustering](images/Customer_Segmentation.png)

---

### Hierarchical Clustering Dendrogram

The dendrogram illustrates how customers are merged into clusters and was used to determine the appropriate number of clusters.

![Hierarchical Dendrogram](images/Hierarchical_Dendrogram.png)

---

### Hierarchical Clustering

Customer segmentation obtained using Agglomerative Hierarchical Clustering.

![Hierarchical Clustering](images/Hierarchical_Customer_Segmentation.png)

---

### DBSCAN Clustering

DBSCAN identified dense customer groups and automatically detected noise (outliers), with `eps` chosen using a K-Distance Graph rather than an arbitrary value.

![DBSCAN Clustering](images/DBSCAN_Customer_Segmentation.png)

## Comparison of Algorithms

| Algorithm               | Number of Clusters | Noise Points | Silhouette Score |
| ----------------------- | -----------------: | -----------: | ---------------: |
| K-Means                 |                  5 |            0 |           0.5547 |
| Hierarchical Clustering |                  5 |            0 |           0.5538 |
| DBSCAN                  |                  2 |            8 |           0.3876 |

---

## Key Findings

- K-Means achieved the highest Silhouette Score.
- Hierarchical Clustering produced results very similar to K-Means.
- DBSCAN's `eps` was selected using a K-Distance Graph rather than an arbitrary value; it still underperforms K-Means/Hierarchical here since this dataset's clusters are roughly convex, which favors centroid- and linkage-based methods.
- K-Means provided the most interpretable customer segmentation for this dataset and was used for the final deployed model.

---

## Business Insights

Using K-Means, five customer segments were identified and named based on their income/spending centroids:

- **Target** (High Income, High Spending) — core high-value customers; prioritize retention via loyalty programs.
- **Careful** (High Income, Low Spending) — highest untapped revenue potential; candidates for targeted promotions.
- **Careless** (Low Income, High Spending) — price-sensitive but highly engaged; good fit for value bundles.
- **Sensible** (Low Income, Low Spending) — lower priority for active marketing spend.
- **Standard** (Moderate Income, Moderate Spending) — largest, most "average" group; broad marketing is most efficient here.

These segments help businesses design personalized marketing campaigns, loyalty programs, and promotional strategies.

---

## Project Structure

Mall-Customer-Segmentation/
│
├── data/
│ └── Mall_Customers.csv
│
├── images/
│ ├── Elbow_Method.png
│ ├── Hierarchical_Dendrogram.png
│ ├── Customer_Segmentation.png
│ ├── Hierarchical_Customer_Segmentation.png
│ ├── DBSCAN_Customer_Segmentation.png
│ ├── DBSCAN_KDistance.png
│ └── ...
│
├── models/
│ ├── kmeans_model.pkl
│ └── scaler.pkl
│
├── notebooks/
│ └── Mall_Customer_Segmentation.ipynb
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore


---

## How to Run Locally

```bash
git clone https://github.com/AdiChakote/mall-customer-segmentation.git
cd mall-customer-segmentation
pip install -r requirements.txt
streamlit run app.py
```

---

## Future Improvements

- Hyperparameter tuning for DBSCAN using additional validation metrics
- Cluster profiling with additional customer attributes (e.g. Age, Gender)
- Extend clustering to 3D (Age + Income + Spending) or PCA-reduced features

---

## Author

**Aditya Sunil Chakote**

GitHub: https://github.com/AdiChakote

LinkedIn: https://www.linkedin.com/in/adityachakote