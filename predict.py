import streamlit as st
import numpy as np
import joblib
import os
import pickle
from catboost import CatBoostRegressor
import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler

def get_value(val, my_dict):
    """Helper function to map values using the provided dictionary"""
    for key, value in my_dict.items():
        if val == key:
            return value

def load_model(model_file):
    """Load the trained model from a .pkl file"""
    loaded_model = joblib.load(open(os.path.join(model_file), 'rb'))
    return loaded_model

def run_predict():
    """Main prediction function"""
    st.subheader('Input Your Data')

    # Collecting user inputs
    carat = st.number_input('Carat Weight:', 0.1, 10.0, 0.1)
    cut = st.selectbox('Cut', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    color = st.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    clarity = st.selectbox('Clarity', ['I1', 'IF', 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2'])
    depth = st.number_input('Diamond Depth Percentage:', 0.1, 100.0, 0.1)
    table = st.number_input('Diamond Table Percentage:', 0.1, 100.0, 0.1)
    x = st.number_input('Diamond Length (X) in mm:', 0.1, 100.0, 0.1)
    y = st.number_input('Diamond Width (Y) in mm:', 0.1, 100.0, 0.1)
    z = st.number_input('Diamond Height (Z) in mm:', 0.1, 100.0, 0.1)

    # Collecting inputs into a dictionary
    result = {
        'Carat': carat,
        'Cut': cut,
        'Color': color,
        'Clarity': clarity,
        'Depth': depth,
        'Table': table,
        'X': x,
        'Y': y,
        'Z': z
    }

    # Convert the dictionary into a DataFrame
    df = pd.DataFrame([result])

    # Map categorical data to one-hot encoding
    cut_mapping = ['Fair', 'Good', 'Ideal', 'Premium', 'Very Good']
    color_mapping = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
    clarity_mapping = ['I1', 'IF', 'SI1', 'SI2', 'VS1', 'VS2', 'VVS1', 'VVS2']

    # Initialize dictionary to hold encoded data
    encoded_data = {
        'carat': df['Carat'][0],
        'depth': df['Depth'][0],
        'table': df['Table'][0],
        'x': df['X'][0],
        'y': df['Y'][0],
        'z': df['Z'][0]
    }

    # Encode categorical features
    for cut in cut_mapping:
        encoded_data[f'cut_{cut}'] = 1 if df['Cut'][0] == cut else 0

    for color in color_mapping:
        encoded_data[f'color_{color}'] = 1 if df['Color'][0] == color else 0

    for clarity in clarity_mapping:
        encoded_data[f'clarity_{clarity}'] = 1 if df['Clarity'][0] == clarity else 0

    # Create DataFrame from encoded data
    df_encoded = pd.DataFrame([encoded_data])
    #st.write(df_encoded)

    # Ensure the correct column order by reindexing
    # Assuming you have training data's columns (e.g., X_train) available for reference
    # df_encoded = df_encoded.reindex(columns=X_train.columns, fill_value=0)  # Uncomment this if X_train.columns are available

    # Load the pre-trained model
    #model = load_model('CatBoostRegressor.pkl')
    model_path = os.path.join(os.getcwd(), "CatBoostRegressor.pkl")
    model = load_model(model_path)

    #if st.button('Predict Price'):
    # Make a prediction
    prediction = model.predict(df_encoded)

    # Display the prediction result
    st.write(f"Predicted Diamond Price: ${prediction[0]:,.2f}")

# Run the app
if __name__ == '__main__':
    run_predict()
