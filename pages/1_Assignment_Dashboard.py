import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📘 Assignment Dashboard (Official)")

df = pd.read_csv("marketing_dataset.csv")
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')


st.sidebar.header("Filters")
platforms = ["All"] + sorted(df["Platform"].unique())
adsets = ["All"] + sorted(df["Adset"].unique())
selected_platform = st.sidebar.selectbox("Platform", platforms)
selected_adset = st.sidebar.selectbox("Adset", adsets)
date_range = st.sidebar.date_input("Date Range", [df["Date"].min(), df["Date"].max()])


dff = df.copy()
if selected_platform != "All":
    dff = dff[dff["Platform"] == selected_platform]
if selected_adset != "All":
    dff = dff[dff["Adset"] == selected_adset]

start, end = date_range
dff = dff[(dff["Date"] >= pd.to_datetime(start)) & (dff["Date"] <= pd.to_datetime(end))]


col1, col2, col3, col4 = st.columns(4)
col1.metric("💰 Total Spend", f"₹{dff['Spend'].sum():,.0f}")
col2.metric("👥 Visitors", f"{dff['Visitors'].sum():,}")
col3.metric("🎯 Leads", f"{dff['Leads'].sum():,}")
col4.metric("🏆 Closures", f"{dff['Closure'].sum():,}")

st.markdown("---")


colA, colB = st.columns(2)
with colA:
    fig = px.line(dff, x="Date", y="Spend", color="Platform", title="Daily Spend")
    st.plotly_chart(fig, use_container_width=True)

with colB:
    fig = px.line(dff, x="Date", y="Visitors", color="Platform", title="Daily Visitors")
    st.plotly_chart(fig, use_container_width=True)

colC, colD = st.columns(2)
with colC:
    fig = px.line(dff, x="Date", y="Leads", color="Platform", title="Daily Leads")
    st.plotly_chart(fig, use_container_width=True)

with colD:
    fig = px.line(dff, x="Date", y="Closure", color="Platform", title="Daily Closure")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


st.subheader("📌 Spend vs Leads (Scatter Plot)")
fig = px.scatter(dff, x="Spend", y="Leads", color="Platform", size="Visitors")
st.plotly_chart(fig, use_container_width=True)


st.subheader("📌 Average Closure per Platform")
avg_closure = df.groupby("Platform")["Closure"].mean().reset_index()
fig = px.bar(avg_closure, x="Platform", y="Closure", title="Avg Closure by Platform")
st.plotly_chart(fig, use_container_width=True)


st.subheader("🔽 Funnel Summary")
funnel = {
    "Stage": ["Visitors", "Leads", "SiteVisits", "Closure"],
    "Value": [
        df["Visitors"].sum(),
        df["Leads"].sum(),
        df["SiteVisits"].sum(),
        df["Closure"].sum(),
    ]
}
f_df = pd.DataFrame(funnel)
fig = px.funnel(f_df, x="Value", y="Stage", title="Marketing Funnel")
st.plotly_chart(fig, use_container_width=True)
