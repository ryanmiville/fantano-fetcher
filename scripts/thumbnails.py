import scrapetube
import requests

videos = scrapetube.get_channel(channel_url="https://www.youtube.com/c/theneedledrop")
videos = (v for v in videos if v["title"]["runs"][0]["text"].endswith("ALBUM REVIEW"))

for v in videos:
    id = v["videoId"]
    tn = v["thumbnail"]["thumbnails"][0]["url"]
    r = requests.get(tn)
    with open(f"thumbnails/{id}.jpg", "wb") as f:
        f.write(r.content)