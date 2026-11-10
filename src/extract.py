import requests


def extract_weather(latitude=44.8176, longitude=20.4633):
    """Povlaci satne vremenske podatke sa Open-Meteo API-ja."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto",
    }

    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = extract_weather()
    print(data["hourly"]["time"][:3])
    print(data["hourly"]["temperature_2m"][:3])