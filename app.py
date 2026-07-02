
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Planet Detector", page_icon="🪐", layout="centered")

# Load files
model = joblib.load("planet_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoder = joblib.load("label_encoder.pkl")
data = pd.read_csv("cumulative_dataset.csv")

st.title("🪐 Planet Detector")
st.write("Search using **Kepler Name**, **KOI Name**, or **Star ID (KepID)**.")

query = st.text_input("Enter Kepler Name / KOI Name / KepID")

if st.button("Predict"):

    if query.strip() == "":
        st.warning("Please enter a value.")

    else:
        q = query.strip().lower()

        result = data[
            data["kepoi_name"].astype(str).str.lower().eq(q) |
            data["kepler_name"].fillna("").astype(str).str.lower().eq(q) |
            data["kepid"].astype(str).eq(query.strip())
        ]

        if len(result) == 0:
            st.error("Planet / Star not found in NASA dataset.")

        else:

            row = result.iloc[0]

            features = [[
                row["koi_period"],
                row["koi_duration"],
                row["koi_depth"],
                row["koi_prad"],
                row["koi_sma"],
                row["koi_teq"],
                row["koi_impact"],
                row["koi_model_snr"],
                row["koi_steff"],
                row["koi_srad"]
            ]]

            features = scaler.transform(features)

            pred = model.predict(features)[0]
            prediction = label_encoder.inverse_transform([pred])[0]

            st.success(f"Prediction: {prediction}")

            st.subheader("Object Details")

            st.write("**Kepler Name:**", row["kepler_name"])
            st.write("**KOI Name:**", row["kepoi_name"])
            st.write("**Star ID:**", row["kepid"])
            st.write("**Orbital Period (days):**", row["koi_period"])
            st.write("**Transit Duration (hours):**", row["koi_duration"])
            st.write("**Transit Depth (ppm):**", row["koi_depth"])
            st.write("**Planet Radius (Earth Radii):**", row["koi_prad"])
            st.write("**Equilibrium Temperature (K):**", row["koi_teq"])
