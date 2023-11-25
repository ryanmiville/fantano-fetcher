from fastai.vision.all import *
import os


ids = ["SNmWrEFCv8c", "LwbUvvxf2I8", "O1k4bQhCx5Y"]


def get_thumbnail_path(id):
    o = os.path.join("thumbnails/other", id + ".jpg")
    y = os.path.join("thumbnails/yellow", id + ".jpg")
    return o if os.path.exists(o) else y


p = get_thumbnail_path(ids[2])
img = PILImage.create(p)

learner = load_learner("thumbnails/ff.pkl")
label, idx, probs = learner.predict(img)
