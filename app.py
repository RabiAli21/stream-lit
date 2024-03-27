{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "736cd745",
   "metadata": {
    "ExecuteTime": {
     "end_time": "2024-03-27T09:23:52.456784Z",
     "start_time": "2024-03-27T09:23:47.165153Z"
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-03-27 14:53:52.409 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\user\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import pandas as pd\n",
    "\n",
    "\n",
    "rf_model = joblib.load('CO2_emission(RF).joblib')\n",
    "\n",
    "\n",
    "def main():\n",
    "    st.title('Random Forest Model Deployment')\n",
    "\n",
    "    # Add user input components\n",
    "    st.sidebar.header('User Input Features')\n",
    "    engine_size = st.sidebar.slider('Engine Size', 1.0, 10.0, 5.0)\n",
    "    cylinders = st.sidebar.slider('Cylinders', 1, 12, 4)\n",
    "    fuel_consumption = st.sidebar.slider('Fuel Consumption (L/100km)', 0.0, 30.0, 10.0)\n",
    "\n",
    "    # Create a dictionary from user inputs\n",
    "    input_data = {\n",
    "        'engine_size': [engine_size],\n",
    "        'cylinders': [cylinders],\n",
    "        'fuel_consumption_comb(l/100km)': [fuel_consumption]\n",
    "    }\n",
    "\n",
    "    # Convert dictionary to DataFrame\n",
    "    input_df = pd.DataFrame(input_data)\n",
    "\n",
    "    # Make prediction using the loaded model\n",
    "    prediction = rf_model.predict(input_df)\n",
    "\n",
    "    # Display prediction\n",
    "    st.subheader('Prediction')\n",
    "    st.write('CO2 Emissions:', prediction)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "39d1e2cd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
