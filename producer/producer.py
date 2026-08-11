from datetime import datetime
import random


sensors = {
    "sensor_001": "warehouse_A",
    "sensor_002": "warehouse_A",
    "sensor_003": "warehouse_B"
}


for sensor_id, location in sensors.items():

    event = {
        "sensor_id": sensor_id,
        "timestamp": datetime.now().isoformat(),
        "temperature": round(random.uniform(65, 80), 1),
        "humidity": round(random.uniform(30, 60), 1),
        "battery_level": random.randint(80, 100),
        "location": location
    }

    print(event)