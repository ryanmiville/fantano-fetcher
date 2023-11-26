from datetime import date
from sqlalchemy import create_engine
from sqlalchemy import text
from dotenv import load_dotenv
import pandas as pd

import os

load_dotenv()

_host = os.getenv("DB_HOST")
_user = os.getenv("DB_USERNAME")
_passwd = os.getenv("DB_PASSWORD")
_db = os.getenv("DB_NAME")

_con_str = f"mysql+mysqlconnector://{_user}:{_passwd}@{_host}/{_db}"

_engine = create_engine(_con_str, echo=True)


def most_recent_publish_date() -> date:
    with _engine.connect() as conn:
        sql = text("select max(publish_date) from reviews")
        results = conn.execute(sql)
        return results.fetchone()[0]


def insert_reviews(df: pd.DataFrame):
    df["yellow_flannel"] = df["yellow_flannel"].astype(int)
    df["publish_date"] = pd.to_datetime(df["publish_date"])
    df.to_sql("reviews", con=_engine, if_exists="append", index=False)
