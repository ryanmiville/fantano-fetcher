# %% [markdown]
# # Yellow Flannel Classifer
# 
# Creates a model using theneedledrop YouTube thumbnails to fine-tune a pretrained model using 🤗 Transformers.

# %%
from multiprocessing import freeze_support
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from pathlib import Path
import torch
import pytorch_lightning as pl
from huggingface_hub import HfApi, HfFolder, Repository, notebook_login
from torch.utils.data import DataLoader, random_split
from torchmetrics import Accuracy
from torchvision.datasets import ImageFolder
from torchvision import transforms
from transformers import ViTFeatureExtractor, ViTForImageClassification


if __name__ == '__main__':
	freeze_support()
# %%
class LimitedImageFolder(ImageFolder):
    def __init__(self, root, transform=None, target_transform=None, limit_per_class=150):
        super(LimitedImageFolder, self).__init__(root, transform, target_transform)
        self.limit_per_class = limit_per_class
        self._limit_dataset()

    def _limit_dataset(self):
        class_counts = dict()
        new_samples = []
        for sample, target in self.samples:
            if target not in class_counts:
                class_counts[target] = 0
            if class_counts[target] < self.limit_per_class:
                new_samples.append((sample, target))
                class_counts[target] += 1
        self.samples = new_samples


# %%

data_root = "./data"

# transform = transforms.Compose([
#     transforms.Resize((32, 32)),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
# ])

ds = LimitedImageFolder(root=data_root, limit_per_class=150)

# %%
train_size = int(0.8 * len(ds))
val_size = len(ds) - train_size
train_dataset, val_dataset = random_split(ds, [train_size, val_size])

# %% [markdown]
# ### Preparing Labels for Our Model's Config
# 
# By adding `label2id` + `id2label` to our model's config, we'll get friendlier labels in the inference API.

# %%
label2id = {}
id2label = {}

for i, class_name in enumerate(ds.classes):
    label2id[class_name] = str(i)
    id2label[str(i)] = class_name

# %% [markdown]
# ### Image Classification Collator
# 
# To apply our transforms to images, we'll use a custom collator class. We'll initialize it using an instance of `ViTFeatureExtractor` and pass the collator instance to `torch.utils.data.DataLoader`'s `collate_fn` kwarg.

# %%
class ImageClassificationCollator:
    def __init__(self, feature_extractor):
        self.feature_extractor = feature_extractor
 
    def __call__(self, batch):
        encodings = self.feature_extractor([x[0] for x in batch], return_tensors='pt')
        encodings['labels'] = torch.tensor([x[1] for x in batch], dtype=torch.long)
        return encodings 

# %% [markdown]
# ### Init Feature Extractor, Model, Data Loaders

# %%
feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224-in21k')
model = ViTForImageClassification.from_pretrained(
    'google/vit-base-patch16-224-in21k',
    num_labels=len(label2id),
    label2id=label2id,
    id2label=id2label
)
collator = ImageClassificationCollator(feature_extractor)
train_loader = DataLoader(train_dataset, batch_size=32, collate_fn=collator, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, collate_fn=collator)

# %% [markdown]
# # Training
# 
# ⚡ We'll use [PyTorch Lightning](https://pytorchlightning.ai/) to fine-tune our model.

# %%
class Classifier(pl.LightningModule):

    def __init__(self, model, lr: float = 2e-5, **kwargs):
        super().__init__()
        self.save_hyperparameters('lr', *list(kwargs))
        self.model = model
        self.forward = self.model.forward
        self.val_acc = Accuracy(
            task='binary',
            num_classes=model.config.num_labels
        )

    def training_step(self, batch, batch_idx):
        outputs = self(**batch)
        self.log(f"train_loss", outputs.loss)
        return outputs.loss

    def validation_step(self, batch, batch_idx):
        outputs = self(**batch)
        self.log(f"val_loss", outputs.loss)
        acc = self.val_acc(outputs.logits.argmax(1), batch['labels'])
        self.log(f"val_acc", acc, prog_bar=True)
        return outputs.loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.hparams.lr)

# %%
pl.seed_everything(42)
classifier = Classifier(model, lr=2e-5)
trainer = pl.Trainer(accelerator='cpu', precision='bf16-mixed', max_epochs=4)
trainer.fit(classifier, train_loader, val_loader)

# %%
val_batch = next(iter(val_loader))
outputs = model(**val_batch)
print('Preds: ', outputs.logits.softmax(1).argmax(1))
print('Labels:', val_batch['labels'])

# %%
model.save_pretrained("./model")
