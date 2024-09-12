import random

def get_soil_moisture():
    # Dummy function
    return random.uniform(20, 50)

def get_temperature():
    # Dummy function
    return random.uniform(25, 40)

# Uncomment and use the real functions to collect data from Raspberry Pi:
# import Adafruit_DHT  # Assuming you're using a DHT sensor
# def get_soil_moisture():
#     # Add Raspberry Pi code to read from soil moisture sensor
#     pass
#
# def get_temperature():
#     # Add Raspberry Pi code to read from temperature sensor
#     pass
