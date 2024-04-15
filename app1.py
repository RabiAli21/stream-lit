import streamlit as st
import joblib
import pandas as pd

# Load the trained Random Forest model
rf_model = joblib.load('CO2_emission(RF).joblib')

# Define the Streamlit app
def main():
    st.title('Random Forest Model Deployment')

    # Add user input components
    st.sidebar.header('User Input Features')
    engine_size = st.sidebar.slider('Engine Size', 1.0, 10.0, 5.0)
    cylinders = st.sidebar.slider('Cylinders', 1, 12, 4)
    fuel_consumption = st.sidebar.slider('Fuel Consumption (L/100km)', 0.0, 30.0, 10.0)

    # Create a dictionary from user inputs
    input_data = {
        'engine_size': [engine_size],
        'cylinders': [cylinders],
        'fuel_consumption_comb(l/100km)': [fuel_consumption]
    }

    # Convert dictionary to DataFrame
    input_df = pd.DataFrame(input_data)

    # Make prediction using the loaded model
    prediction = rf_model.predict(input_df)

    # Display prediction
    st.subheader('Prediction')
    st.write('CO2 Emissions:', prediction)

if __name__ == '__main__':
    main()
