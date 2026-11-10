import pandas as pd

from transform import transform_weather
from quality import check_quality


def make_raw():
    return {
        "hourly": {
            "time": [
                "2026-11-10T00:00",
                "2026-11-10T01:00",
                "2026-11-10T01:00",  # duplikat
                "2026-11-10T02:00",
            ],
            "temperature_2m": [5.0, 6.0, 6.0, None],  # poslednja fali
            "relative_humidity_2m": [80, 75, 75, 70],
            "wind_speed_10m": [10.0, 12.0, 12.0, 9.0],
        }
    }


def test_removes_duplicates_and_missing_values():
    df = transform_weather(make_raw())
    assert len(df) == 2


def test_adds_city_column():
    df = transform_weather(make_raw(), city="Nis")
    assert (df["city"] == "Nis").all()


def test_recorded_at_is_datetime():
    df = transform_weather(make_raw())
    assert pd.api.types.is_datetime64_any_dtype(df["recorded_at"])


def test_quality_passes_on_clean_data():
    df = transform_weather(make_raw())
    assert check_quality(df) == []


def test_quality_catches_bad_humidity():
    df = transform_weather(make_raw())
    df.loc[df.index[0], "humidity_pct"] = 150
    assert "Vlaznost je van opsega 0-100%" in check_quality(df)