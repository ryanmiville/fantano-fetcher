from http.server import BaseHTTPRequestHandler
import api._db as db
from api._yt import get_reviews_after
from api._hf import wearing_yellow_flannel


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        most_recent = db.most_recent_publish_date()
        reviews = get_reviews_after(most_recent)

        for review in reviews:
            review["yellow_flannel"] = wearing_yellow_flannel(review["thumbnail_url"])

        db.insert_reviews(reviews)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"{len(reviews)} reviews added".encode("utf-8"))
        return
