import scrapetube
import csv

videos = scrapetube.get_channel(channel_url="https://www.youtube.com/c/theneedledrop")
videos = (v for v in videos if v["title"]["runs"][0]["text"].endswith("ALBUM REVIEW"))

with open("videos.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for v in videos:
        id = v["videoId"]
        url = f"https://www.youtube.com/watch?v={id}"
        writer.writerow([url])
