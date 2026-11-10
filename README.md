# Automated Data Pipeline

ETL pipeline that pulls hourly weather data from the Open-Meteo API,
cleans it with Pandas, validates it, and loads it into PostgreSQL.

## Architecture

Extract (requests) -> Transform (pandas) -> Data quality checks -> Load (SQLAlchemy + PostgreSQL)

## Features

- Idempotent loads: re-running the pipeline updates existing rows instead of duplicating them
- Data quality checks run before loading; bad data never reaches the database
- Credentials stored in .env, never in code
- Unit tests with pytest

## Tech stack

Python, Requests, Pandas, SQLAlchemy, PostgreSQL, pytest

## Setup

1. Create a PostgreSQL database named weather_db
2. Run sql/create_tables.sql in that database
3. Create a .env file with DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
4. Install dependencies: pip install -r requirements.txt
5. Run the pipeline: python src/main.py
6. Run tests: python -m pytest

## Project structure

- src/extract.py: fetch data from the API
- src/transform.py: clean and reshape data
- src/quality.py: data quality checks
- src/load.py: upsert into PostgreSQL
- src/main.py: runs the full pipeline
- tests/: unit tests

## Next steps

Schedule the pipeline with Apache Airflow and add more cities.