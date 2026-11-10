import pandas as pd


def transform_weather(raw_data, city="Beograd"):
    """Pretvara sirovi JSON u ociscenu tabelu."""
    hourly = raw_data["hourly"]

    df = pd.DataFrame({
        "recorded_at": hourly["time"],
        "temperature_c": hourly["temperature_2m"],
        "humidity_pct": hourly["relative_humidity_2m"],
        "wind_speed_kmh": hourly["wind_speed_10m"],
    })

    # tekst -> pravi datum i vreme
    df["recorded_at"] = pd.to_datetime(df["recorded_at"])

    # ukloni redove gde nedostaje neka vrednost
    df = df.dropna()

    # ukloni duplikate po vremenu
    df = df.drop_duplicates(subset="recorded_at")

    # dodaj kolonu sa gradom
    df["city"] = city

    return df


if __name__ == "__main__":
    from extract import extract_weather

    raw = extract_weather()
    df = transform_weather(raw)
    print(df.head())
    print(df.shape)