database = {
    "MAF": {
        "name": "MAF",
        "description": "Quality of Filter",
        "unit": "gm/s",
        "min_value": 0,
        "max_value": 400,
        "Cold Starting": {
            "normal_min": 18,
            "normal_max": 3,
        },
        "Warm Idling": {
            "normal_min": 18,
            "normal_max": 3,
        },
        "Acceleration": {
            "normal_min": 94,
            "normal_max": 45,
        },
        "Deceleration": {
            "normal_min": 94,
            "normal_max": 45,
        },
        "Cruise": {
            "normal_min": 94,
            "normal_max": 45,
        },
        "measurement": "Mass of intake air",
        "source": "Mass Airflow Sensor",
    },
    "MAP": {
        "name": "MAP",
        "description": "Manifold Air Pressure",
        "unit": "kPa",
        "min_value": 0,
        "max_value": 320,
        "Cold Starting": {
            "normal_min": 90,
            "normal_max": 100,
        },
        "Warm Idling": {
            "normal_min": 90,
            "normal_max": 100,
        },
        "Acceleration": {
            "normal_min": 110,
            "normal_max": 135,
        },
        "Deceleration": {
            "normal_min": 110,
            "normal_max": 135,
        },
        "Cruise": {
            "normal_min": 110,
            "normal_max": 135,
        },
        "measurement": "Mass of intake air",
        "source": "Mass Airflow Sensor",
    },
}
