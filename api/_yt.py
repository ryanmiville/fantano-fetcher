import scrapetube
from pytube import YouTube
import re
from datetime import date
import pandas as pd


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


def _parse_description(df) -> pd.DataFrame:
    # Derive column 'derivedCol' from column: 'title'
    # Transform "title" as per the following examples:
    #   HMLTD - The Worm ALBUM REVIEW ==> HMLTD
    #   Depeche Mode - Memento Mori ALBUM REVIEW ==> Depeche Mode
    df.insert(2, "artist", df["title"].str.split(" -").str[0].str.strip())
    # Derive column 'derivedCol' from column: 'title'
    # Transform "title" as per the following examples:
    #   HMLTD - The Worm ALBUM REVIEW ==> The Worm
    #   Depeche Mode - Memento Mori ALBUM REVIEW ==> Memento Mori
    df.insert(
        3,
        "album",
        df["title"]
        .str.split(" - ")
        .str[1]
        .str.strip()
        .str.removesuffix(" ALBUM REVIEW"),
    )
    df.loc[:, "description"] = df["description"].str.replace("\\n", "\n")
    # rename all columns to be snake_case
    df = df.rename(
        columns={
            "videoId": "video_id",
            "thumbnailUrl": "thumbnail_url",
            "publishDate": "publish_date",
            "watchUrl": "watch_url",
        }
    )
    df["rating"] = df["description"].str.extract(r"\n(\d+)/10")
    df["rating"] = pd.to_numeric(df["rating"])
    return df


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
                "videoId": yt.video_id,
                "title": yt.title,
                "description": desc,
                "thumbnailUrl": yt.thumbnail_url,
                "publishDate": publish_date,
                "watchUrl": yt.watch_url,
            }
            yield vid


def get_reviews_after(date: date):
    df = pd.DataFrame(_get_videos_after(date))
    return _parse_description(df)
