import logging

from extract import extract_weather
from transform import transform_weather
from quality import check_quality
from load import load_weather

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)


def run_pipeline():
    log.info("Extract: povlacim podatke sa API-ja")
    raw = extract_weather()

    log.info("Transform: cistim podatke")
    df = transform_weather(raw)

    log.info("Provera kvaliteta: %s redova", len(df))
    problems = check_quality(df)
    if problems:
        for p in problems:
            log.error(p)
        raise ValueError("Podaci nisu prosli proveru kvaliteta")

    n = load_weather(df)
    log.info("Load: upisano %s redova u bazu", n)


if __name__ == "__main__":
    run_pipeline()