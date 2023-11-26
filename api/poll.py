from http.server import BaseHTTPRequestHandler
from api._db import most_recent_publish_date, insert_reviews
from api._yt import get_reviews_after
from api._hf import wearing_yellow_flannel


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        most_recent = most_recent_publish_date()
        df = get_reviews_after(most_recent)
        df["yellow_flannel"] = df["thumbnail_url"].apply(wearing_yellow_flannel)
        insert_reviews(df)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"{len(df)} reviews added".encode("utf-8"))
        return
