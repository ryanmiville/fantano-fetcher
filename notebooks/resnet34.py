from fastai.vision.all import *

from huggingface_hub import push_to_hub_fastai

path = "thumbnails"

dls = ImageDataLoaders.from_path_func(
    path,
    get_image_files(path),
    valid_pct=0.2,
    seed=42,
    label_func=parent_label,
    item_tfms=Resize(224),
)

learn = vision_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(6)


push_to_hub_fastai(learner=learn, repo_id="ryanmiville/fantano-yellow-flannel")
