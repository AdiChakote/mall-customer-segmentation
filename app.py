import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px


st.set_page_config(page_title="Mall Customer Segmentation", layout="centered")


@st.cache_resource
def load_artifacts():
    kmeans = joblib.load("models/kmeans_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return kmeans, scaler

@st.cache_data
def load_data():
    df = pd.read_csv("data/Mall_Customers.csv")
    return df

kmeans, scaler = load_artifacts()
df = load_data()

X = df[["Annual Income (k$)", "Spending Score (1-100)"]]
X_scaled = scaler.transform(X)
df["Cluster"] = kmeans.predict(X_scaled)

income_median = df["Annual Income (k$)"].median()
spending_median = df["Spending Score (1-100)"].median()

def label_segment(income, spending):
    income_high = income >= income_median
    spending_high = spending >= spending_median
    if abs(income - income_median) <= income_median * 0.15 and abs(spending - spending_median) <= spending_median * 0.15:
        return "Standard (Moderate Income, Moderate Spending)"
    if income_high and spending_high:
        return "Target (High Income, High Spending)"
    elif income_high and not spending_high:
        return "Careful (High Income, Low Spending)"
    elif not income_high and spending_high:
        return "Careless (Low Income, High Spending)"
    else:
        return "Sensible (Low Income, Low Spending)"

segment_descriptions = {
    "Target (High Income, High Spending)": "Core high-value customers. Prioritize retention with loyalty programs and personalized offers.",
    "Careful (High Income, Low Spending)": "Highest untapped revenue potential. Good candidates for targeted promotions to increase engagement.",
    "Careless (Low Income, High Spending)": "Price-sensitive but highly engaged. Good fit for value bundles or installment options.",
    "Sensible (Low Income, Low Spending)": "Lower priority for active marketing spend; monitor for lifecycle changes.",
    "Standard (Moderate Income, Moderate Spending)": "The largest, most \"average\" group. Broad, general marketing is most efficient here.",
}

cluster_centroids = df.groupby("Cluster")[["Annual Income (k$)", "Spending Score (1-100)"]].mean()
cluster_segment_map = {
    cluster: label_segment(row["Annual Income (k$)"], row["Spending Score (1-100)"])
    for cluster, row in cluster_centroids.iterrows()
}
df["Segment"] = df["Cluster"].map(cluster_segment_map)


st.title("🛍️ Mall Customer Segmentation")
st.write(
    "This app segments customers using K-Means clustering trained on Annual Income "
    "and Spending Score. Enter a customer's details below to see which segment they fall into."
)

st.subheader("Enter Customer Details")
col1, col2 = st.columns(2)

with col1:
    income_input = st.slider("Annual Income (k$)", min_value=0, max_value=150, value=60, step=1)

with col2:
    spending_input = st.slider("Spending Score (1-100)", min_value=0, max_value=100, value=50, step=1)


user_scaled = scaler.transform([[income_input, spending_input]])
user_cluster = kmeans.predict(user_scaled)[0]
user_segment = cluster_segment_map[user_cluster]

st.subheader("Predicted Segment")
st.success(f"**{user_segment}**")
st.write(segment_descriptions[user_segment])


st.subheader("Where This Customer Falls Among Existing Customers")

fig = px.scatter(
    df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    color="Segment",
    opacity=0.6,
    title="Customer Segments",
)

fig.add_scatter(
    x=[income_input],
    y=[spending_input],
    mode="markers",
    marker=dict(size=16, color="black", symbol="star"),
    name="New Customer",
)

st.plotly_chart(fig, use_container_width=True)

with st.expander("View All Segment Definitions"):
    summary = cluster_centroids.copy()
    summary["Segment"] = summary.index.map(cluster_segment_map)
    summary["Customer Count"] = df["Cluster"].value_counts().sort_index()
    st.dataframe(summary.reset_index(drop=True))