import json
from pytube import YouTube
import csv


urls = []
with open("videos.csv", newline="") as f:
    reader = csv.reader(f)
    urls = [row[0] for row in reader]

with open("descriptions.jsonl", "w") as f:
    for url in urls:
        yt = YouTube(url)
        vid = {
            "videoId": yt.video_id,
            "title": yt.title,
            "description": yt.description,
            "thumbnailUrl": yt.thumbnail_url,
            "publishDate": yt.publish_date.strftime("%Y-%m-%d"),
            "watchUrl": yt.watch_url,
        }
        json.dump(vid, f)
        f.write("\n")
