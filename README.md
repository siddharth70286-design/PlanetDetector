# 🪐 Planet Detector

A Machine Learning web application that predicts the status of Kepler exoplanets using NASA's Kepler Objects of Interest (KOI) dataset.

## Features

- Search by Kepler Name
- Search by KOI Name
- Search by Star ID (KepID)
- Predicts:
  - CONFIRMED
  - CANDIDATE
  - FALSE POSITIVE

## Dataset

NASA Exoplanet Archive
Kepler Objects of Interest (KOI)

## Machine Learning

Model: Random Forest Classifier

Accuracy: ~78.6%

## Run Locally

pip install -r requirements.txt

streamlit run app.py
