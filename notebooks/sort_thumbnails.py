import pandas as pd
import os

desc = pd.read_json("descriptions_db_ready.jsonl", lines=True)

thumbnails = [i.split(".")[0] for i in os.listdir("thumbnails")]
# thumbnails = [i for i in os.listdir("thumbnails")]
print(len(thumbnails))
thumbnails[0]


row = desc.iloc[0]

import shutil


def sort_thumbnail(row):
    thumbnail_name = row["video_id"] + ".jpg"  # assuming thumbnails are jpg files
    source_path = os.path.join("thumbnails", thumbnail_name)

    if row["yellow_flannel"]:
        target_path = os.path.join("thumbnails/yellow", thumbnail_name)
    else:
        target_path = os.path.join("thumbnails/other", thumbnail_name)

    if os.path.exists(source_path):
        shutil.move(source_path, target_path)


for _, row in desc.iterrows():
    sort_thumbnail(row)

dir = os.listdir("thumbnails")

yellow = os.listdir("thumbnails/yellow")
other = os.listdir("thumbnails/other")
