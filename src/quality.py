def check_quality(df):
    """Vraca listu problema. Prazna lista znaci da je sve u redu."""
    problems = []

    if df.empty:
        problems.append("Tabela je prazna")

    if not df["temperature_c"].between(-60, 60).all():
        problems.append("Temperatura je van realnog opsega (-60 do 60 C)")

    if not df["humidity_pct"].between(0, 100).all():
        problems.append("Vlaznost je van opsega 0-100%")

    if (df["wind_speed_kmh"] < 0).any():
        problems.append("Brzina vetra je negativna")

    if df.duplicated(subset=["city", "recorded_at"]).any():
        problems.append("Postoje duplikati (grad + vreme)")

    return problems