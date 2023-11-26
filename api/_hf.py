from huggingface_hub import InferenceClient


def wearing_yellow_flannel(thumbnail_url: str) -> bool:
    client = InferenceClient(model="ryanmiville/fantano-yellow-flannel")
    output = client.image_classification(thumbnail_url)
    label = max(output, key=lambda x: x["score"])["label"]
    return label == "yellow"
