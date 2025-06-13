import streamlit as st
import numpy as np
import pickle
import json
import base64

# ✅ Set page config
st.set_page_config(page_title="Bangalore House Price Predictor")

# ✅ Background image function (uses base64)
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

        /* Label text styling */
        label {{
            color: black !important;
            font-weight: 600;
            font-size: 18px !important;
        }}

        /* Input and select text */
        input, select, textarea {{
            color: black !important;
            font-size: 17px !important;
        }}

        /* Placeholder text — force white color */
        input::placeholder {{
            color: white !important;
        }}

        div[data-baseweb="input"] input {{
            color: white !important;
        }}

        /* Button styling */
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



# ✅ Set the background image (ensure Image.png is in the same directory)
set_background("Image.png")

# 📦 Load model and columns
with open("mode.pickle", "rb") as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

locations = [col for col in data_columns if col not in ["total_sqft", "bath", "bhk"]]

# 🔮 Prediction function
def predict_price(location, sqft, bath, bhk):
    x = np.zeros(len(data_columns))
    x[data_columns.index("total_sqft")] = sqft
    x[data_columns.index("bath")] = bath
    x[data_columns.index("bhk")] = bhk
    if location in data_columns:
        x[data_columns.index(location)] = 1
    return round(max(model.predict([x])[0], 0), 2)

# 🖼️ App Title
st.markdown("<h1 style='text-align: center; font-size: 36px;'>🏠 Bangalore House Price Predictor</h1>", unsafe_allow_html=True)

# ✍️ Input Fields
location = st.selectbox("Select Location", sorted(locations))
sqft = st.number_input("Enter Total Square Feet", min_value=300)
bath = st.number_input("Enter Number of Bathrooms", min_value=1, step=1)
bhk = st.number_input("Enter Number of BHK", min_value=1, step=1)

# 🔘 Predict Button
if st.button("Predict Price"):
    price = predict_price(location, sqft, bath, bhk)
    st.success(f"🏷️ Estimated Price: ₹ {price} Lakhs")
