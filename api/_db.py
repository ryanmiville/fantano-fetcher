from datetime import date
from sqlalchemy import create_engine
from sqlalchemy import text, Table, MetaData, insert
from dotenv import load_dotenv

import os

load_dotenv()

_host = os.getenv("PLANETSCALE_DB_HOST")
_user = os.getenv("PLANETSCALE_DB_USERNAME")
_passwd = os.getenv("PLANETSCALE_DB_PASSWORD")
_db = os.getenv("PLANETSCALE_DB")

_con_str = f"mysql+mysqlconnector://{_user}:{_passwd}@{_host}/{_db}"

_engine = create_engine(_con_str, echo=True)


def most_recent_publish_date() -> date:
    with _engine.connect() as conn:
        sql = text("select max(publish_date) from reviews")
        results = conn.execute(sql)
        return results.fetchone()[0]


def insert_reviews(reviews: list[dict]):
    metadata = MetaData()
    reviews_table = Table("reviews", metadata, autoload_with=_engine)

    with _engine.connect() as connection:
        for review in reviews:
            # Convert boolean to int for 'yellow_flannel'
            review["yellow_flannel"] = int(review["yellow_flannel"])
            stmt = insert(reviews_table).values(review)
            connection.execute(stmt)
