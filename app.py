
import streamlit as st
import requests
import pandas as pd
import numpy as np

# URL to API
API_URL = "https://taxifare-970234754562.europe-west2.run.app/predict"

# Function to call the API and get the prediction
def get_prediction(pickup_datetime, pickup_longitude, pickup_latitude,
                   dropoff_longitude, dropoff_latitude, passenger_count):
    # Prepare the data for the API request
    data = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    # Make the API request
    response = requests.get(API_URL, params=data)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json().get("prediction")
    else:
        st.error("Error in API request")
        return None

# Streamlit app layout
st.title("Taxi Fare Prediction")

# Input fields for the parameters
pickup_datetime = st.datetime_input("Date and Time", datetime.now())
pickup_longitude = st.number_input("Pickup Longitude", format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", format="%.6f")
passenger_count = st.number_input("Passenger Count", min_value=1, step=1)

# Button to get the prediction
if st.button("Predict"):
    prediction = get_prediction(pickup_datetime, pickup_longitude, pickup_latitude,
                                dropoff_longitude, dropoff_latitude, passenger_count)
    if prediction is not None:
        st.success(f"The predicted fare is ${prediction:.2f}")

# Adding a map
st.map(data=[(pickup_latitude, pickup_longitude), (dropoff_latitude, dropoff_longitude)],
       zoom=12)
