import streamlit as st
import numpy as np
import pickle
import json
import base64

# ✅ Set page config
st.set_page_config(page_title="Bangalore House Price Predictor")

# ✅ Background image function
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: black;
            font-size: 18px;
        }}
        label {{
            color: black !important;
            font-weight: 600;
            font-size: 18px !important;
        }}
        input, select, textarea {{
            color: black !important;
            font-size: 17px !important;
        }}
        input::placeholder {{
            color: white !important;
        }}
        div[data-baseweb="input"] input {{
            color: white !important;
        }}
        .stButton > button {{
            background-color: black !important;
            color: white !important;
            font-size: 18px !important;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Set background image
set_background("Image.png")

# 📦 Load model and columns
with open("mode.pickle", "rb") as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

# 🔍 Extract options
area_types = ["Carpet  Area", "Plot  Area", "Super built-up  Area", "Built-up  Area"]  # Add others if needed
locations = [col for col in data_columns if col not in ["total_sqft", "bath", "bhk"] + area_types]

# 🔮 Prediction function
def predict_price(area_type, location, sqft, bath, bhk):
    x = np.zeros(len(data_columns))
    x[data_columns.index("total_sqft")] = sqft
    x[data_columns.index("bath")] = bath
    x[data_columns.index("bhk")] = bhk
    if location in data_columns:
        x[data_columns.index(location)] = 1
    if area_type in data_columns:
        x[data_columns.index(area_type)] = 1
    return round(max(model.predict([x])[0], 0), 2)

# 🖼️ Title
st.markdown("<h1 style='text-align: center; font-size: 36px;'>🏠 Bangalore House Price Predictor</h1>", unsafe_allow_html=True)

# ✍️ Input Fields
area_type = st.selectbox("Select Area Type", area_types)
location = st.selectbox("Select Location", sorted(locations))
sqft = st.number_input("Enter Total Square Feet", min_value=300)
bath = st.number_input("Enter Number of Bathrooms", min_value=1, step=1)
bhk = st.number_input("Enter Number of BHK", min_value=1, step=1)

# 🔘 Predict
if st.button("Predict Price"):
    price = predict_price(area_type, location, sqft, bath, bhk)
    st.markdown(
        f"""
        <div style='
            background-color: #d4edda;
            padding: 15px;
            border-left: 5px solid #28a745;
            border-radius: 5px;
            font-size: 20px;
            color: #155724;'>
            🏷️ Estimated Price: <span style='color: black; font-weight: bold;'>₹ {price} Lakhs</span>
        </div>
        """,
        unsafe_allow_html=True
    )
