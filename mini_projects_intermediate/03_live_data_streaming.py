# 📌 Mini-Project: Live Data Streaming (Generators)
# 🎯 Goal: Simulate streaming live sensor data using generators

import time
import random

def live_temperature_sensor():
    while True:
        temp = round(random.uniform(20.0, 35.0), 2)  # Simulate temperature
        yield f"🌡️ Temperature: {temp}°C"
        time.sleep(2)  # Simulate delay

# ✅ Using the Generator
sensor = live_temperature_sensor()
for _ in range(5):  # Simulate receiving 5 readings
    print(next(sensor))

# Output (random values):
# 🌡️ Temperature: 24.56°C
# 🌡️ Temperature: 30.12°C
# 🌡️ Temperature: 28.95°C
