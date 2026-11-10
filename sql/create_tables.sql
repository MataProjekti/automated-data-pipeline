CREATE TABLE IF NOT EXISTS weather_hourly (
    city           VARCHAR(100) NOT NULL,
    recorded_at    TIMESTAMP NOT NULL,
    temperature_c  NUMERIC(5,2),
    humidity_pct   NUMERIC(5,2),
    wind_speed_kmh NUMERIC(6,2),
    PRIMARY KEY (city, recorded_at)
);