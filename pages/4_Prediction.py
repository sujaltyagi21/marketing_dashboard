import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error

st.title(" Closure Prediction Using Random Forest")

df = pd.read_csv("marketing_dataset.csv")


le = LabelEncoder()
df["Platform_enc"] = le.fit_transform(df["Platform"])
df["Adset_enc"] = le.fit_transform(df["Adset"])


X = df[["Spend", "Visitors", "Leads", "SiteVisits", "Platform_enc", "Adset_enc"]]
y = df["Closure"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

pred = model.predict(X_test)
st.metric("Model R² Score", f"{r2_score(y_test, pred):.2f}")
st.metric("MAE", f"{mean_absolute_error(y_test, pred):.2f}")


st.subheader("📌 Predict Closures")
spend = st.number_input("Spend")
vis = st.number_input("Visitors")
leads = st.number_input("Leads")
sv = st.number_input("Site Visits")
platform = st.selectbox("Platform", le.classes_)
adset = st.selectbox("Adset", le.classes_)

platform_val = le.transform([platform])[0]
adset_val = le.transform([adset])[0]

if st.button("Predict"):
    val = model.predict([[spend, vis, leads, sv, platform_val, adset_val]])
    st.success(f"Estimated Closures: {val[0]:.2f}")
