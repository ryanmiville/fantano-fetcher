from pytube import Channel
import requests as req


url = "https://www.youtube.com/c/theneedledrop"
c = Channel(url)

videos = (v for v in c.videos_generator() if v.title.endswith("ALBUM REVIEW"))
thumbnails = (v.thumbnail_url for v in videos)

for tn in thumbnails:
    r = req.get(tn)
    with open(f"{tn}.jpg", "wb") as f:
        f.write(r.content)
