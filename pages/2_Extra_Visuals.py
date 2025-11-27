import streamlit as st
import pandas as pd
import plotly.express as px

st.title("✨ Extra Visuals & Bonus Analysis")

df = pd.read_csv("marketing_dataset.csv")


st.subheader("Rolling Avg Visitors Trend")
df["Visitors_Smooth"] = df["Visitors"].rolling(5).mean()
fig = px.line(df, x="Date", y="Visitors_Smooth")
st.plotly_chart(fig, use_container_width=True)
