import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

load_dotenv()


def get_engine():
    """Pravi konekciju ka PostgreSQL bazi iz .env podataka."""
    url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
    )
    return create_engine(url)


INSERT_SQL = text("""
    INSERT INTO weather_hourly
        (city, recorded_at, temperature_c, humidity_pct, wind_speed_kmh)
    VALUES
        (:city, :recorded_at, :temperature_c, :humidity_pct, :wind_speed_kmh)
    ON CONFLICT (city, recorded_at) DO UPDATE SET
        temperature_c  = EXCLUDED.temperature_c,
        humidity_pct   = EXCLUDED.humidity_pct,
        wind_speed_kmh = EXCLUDED.wind_speed_kmh
""")


def load_weather(df):
    """Upisuje tabelu u bazu. Postojece redove azurira, nove dodaje."""
    engine = get_engine()
    records = df.to_dict("records")
    with engine.begin() as conn:
        conn.execute(INSERT_SQL, records)
    return len(records)


if __name__ == "__main__":
    from extract import extract_weather
    from transform import transform_weather

    df = transform_weather(extract_weather())
    n = load_weather(df)
    print(f"Upisano redova: {n}")