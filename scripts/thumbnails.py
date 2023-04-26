from pytube import Channel
import requests as req


url = "https://www.youtube.com/c/theneedledrop"
c = Channel(url)

videos = (v for v in c.videos_generator() if v.title.endswith("ALBUM REVIEW"))

for v in videos:
    tn = v.thumbnail_url
    r = req.get(tn)
    with open(f"{v.title}.jpg", "wb") as f:
        f.write(r.content)
