import os


def label(dir: str, label: int):
    """
    Labels all images in a directory with a label
    """
    with open("labels.csv", "a") as f:
        for filename in os.listdir(dir):
            if not filename.endswith(".jpg"):
                continue
            # strip string of .jpg
            filename = filename[:-4]
            f.write(f"{filename},{label}\n")


with open("labels.csv", "w") as f:
    f.write("filename,yellow\n")

label("thumbnails/yellow", 1)
label("thumbnails", 0)
