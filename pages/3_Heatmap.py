import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🔥 Correlation Heatmap")

df = pd.read_csv("marketing_dataset.csv")

numeric_cols = ["Spend", "Visitors", "Leads", "SiteVisits", "Closure"]
corr = df[numeric_cols].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
st.pyplot(plt)
