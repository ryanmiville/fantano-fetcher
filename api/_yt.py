import scrapetube
from pytube import YouTube
import re
from datetime import date


def _description(full_html) -> str:
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


def _parse_description(videos):
    for video in videos:
        # Derive 'artist' from 'title'
        video["artist"] = video["title"].split(" -")[0].strip()

        # Derive 'album' from 'title'
        album_title = video["title"].split(" - ")[1].strip()
        video["album"] = album_title.removesuffix(" ALBUM REVIEW")

        # Replace '\\n' with '\n' in 'description'
        video["description"] = video["description"].replace("\\n", "\n")

        # Extract rating from description as an integer
        rating_match = re.search(r"\n(\d+)/10", video["description"])
        if rating_match:
            video["rating"] = int(rating_match.group(1))
        else:
            video["rating"] = None

    return videos


def _get_videos_after(date: date):
    videos = scrapetube.get_channel(
        channel_url="https://www.youtube.com/c/theneedledrop"
    )
    for v in videos:
        t = v["title"]["runs"][0]["text"]
        if t.endswith("ALBUM REVIEW"):
            yt = YouTube(f"https://www.youtube.com/watch?v={v['videoId']}")
            publish_date = yt.publish_date.date()
            if publish_date <= date:
                break
            desc = _description(yt.watch_html)
            vid = {
                "video_id": yt.video_id,
                "title": yt.title,
                "description": desc,
                "thumbnail_url": yt.thumbnail_url,
                "publish_date": publish_date,
                "watch_url": yt.watch_url,
            }
            yield vid


def get_reviews_after(date: date):
    videos = _get_videos_after(date)
    return _parse_description(list(videos))
