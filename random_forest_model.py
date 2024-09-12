import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sensors.sensor_functions import get_soil_moisture, get_temperature
import random

# Load historical data
def load_historical_data(file_path='data/chengalpattu_pests.csv'):
    df = pd.read_csv(file_path)
    return df

# Train the RandomForest model
def train_model(data_file='data/chengalpattu_pests.csv'):
    data = load_historical_data(data_file)
    
    # Features are soil moisture and temperature
    X = data[['Soil_Moisture', 'Temperature']]
    y = data['Pest_Type']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Initialize the RandomForestClassifier
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    rf_model.fit(X_train, y_train)
    
    # Test the model
    y_pred = rf_model.predict(X_test)
    
    # Print the accuracy score
    accuracy = accuracy_score(y_test, y_pred)
    
    return rf_model

# Generate random weather data
def generate_random_weather_data():
    temperature = random.uniform(15.0, 35.0)  # Random temperature between 15 and 35 Celsius
    humidity = random.uniform(30.0, 90.0)     # Random humidity between 30% and 90%
    weather_condition = random.choice(['Clear', 'Cloudy', 'Rain', 'Storm'])  # Random weather condition
    return temperature, humidity, weather_condition

# Predict pest infestation based on sensor and weather data
def predict_pest_infestation(model, city="Chengalpattu"):
    # Collect soil moisture and temperature from Raspberry Pi (dummy or actual functions)
    soil_moisture = get_soil_moisture()
    temperature = get_temperature()

    # Generate random weather data
    temp, humidity, weather_condition = generate_random_weather_data()
    print(f"Weather Data - Temperature: {temp}, Humidity: {humidity}")

    # Combine sensor and weather data
    input_data = pd.DataFrame({
        'Soil_Moisture': [soil_moisture],
        'Temperature': [temperature]
    })
    
    # Predict pest infestation
    pest_prediction = model.predict(input_data)
    print(f"Predicted Pest Infestation: {pest_prediction[0]}")

# Main function to train and predict
def main():
    # Train the model
    print("Training the RandomForest model...")
    model = train_model()
    
    # Predict pest infestation using live sensor and random weather data
    print("Fetching live data and predicting pest infestation...")
    predict_pest_infestation(model, city="Chengalpattu")

if __name__ == "__main__":
    main()
