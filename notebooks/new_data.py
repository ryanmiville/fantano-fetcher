import scrapetube
from pytube import YouTube
import re
import json
from tqdm import tqdm

most_recent = "2023-06-24"


def description(full_html):
    y = re.search(r'shortDescription":"', full_html)
    desc = ""
    count = y.start() + 19  # adding the length of the 'shortDescription":"
    while True:
        # get the letter at current index in text
        letter = full_html[count]
        if letter == '"':
            if full_html[count - 1] == "\\":
                # this is case where the letter before is a backslash, meaning it is not real end of description
                desc += letter
                count += 1
            else:
                break
        else:
            desc += letter
            count += 1

    return desc


videos = scrapetube.get_channel(channel_url="https://www.youtube.com/c/theneedledrop")

with open(f"descriptions_after_{most_recent}.jsonl", "w") as f:
    for v in tqdm(videos):
        t = v["title"]["runs"][0]["text"]
        if t.endswith("ALBUM REVIEW"):
            yt = YouTube(f"https://www.youtube.com/watch?v={v['videoId']}")
            publish_date = yt.publish_date.strftime("%Y-%m-%d")
            if publish_date <= most_recent:
                break
            desc = description(yt.watch_html)
            vid = {
                "videoId": yt.video_id,
                "title": yt.title,
                "description": desc,
                "thumbnailUrl": yt.thumbnail_url,
                "publishDate": publish_date,
                "watchUrl": yt.watch_url,
            }
            json.dump(vid, f)
            f.write("\n")
