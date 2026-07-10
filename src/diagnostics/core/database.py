database = {
    "MAF": {
        "name": "MAF",
        "description": "Quality of Filter",
        "unit": "gm/s",
        "min_value": 0,
        "max_value": 400,
        "Cold Starting": {
            "normal_min": 3,
            "normal_max": 18,
        },
        "Warm Idling": {
            "normal_min": 3,
            "normal_max": 18,
        },
        "Acceleration": {
            "normal_min": 45,
            "normal_max": 94,
        },
        "Deceleration": {
            "normal_min": 45,
            "normal_max": 95,
        },
        "Cruise": {
            "normal_min": 45,
            "normal_max": 94,
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
    "Accelerator Pedal Position": {
        "name": "Accelerator Position Sensor",
        "description": "Detects the opening of the accelerator pedal",
        "unit": "%",
        "min_value": 0,
        "max_value": 100,
        "Cold Starting": {
            "normal_min": 0,
            "normal_max": 100,
        },
        "Warm Idling": {
            "normal_min": 0,
            "normal_max": 100,
        },
        "Acceleration": {
            "normal_min": 0,
            "normal_max": 100,
        },
        "Deceleration": {
            "normal_min": 0,
            "normal_max": 100,
        },
        "Cruise": {
            "normal_min": 0,
            "normal_max": 100,
        },
        "measurement": "Opening of the accelerator pedal",
        "source": "Accelerator Pedal Position Sensor",
    },
}
