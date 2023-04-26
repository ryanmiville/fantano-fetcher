from pytube import Channel
import csv


url = "https://www.youtube.com/c/theneedledrop"
c = Channel(url)

videos = (v for v in c.videos_generator() if v.title.endswith("ALBUM REVIEW"))

headers = ["title", "description"]

with open("descriptions.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for v in videos:
        writer.writerow({"title": v.title, "description": v.description})
