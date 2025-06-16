from PIL import Image
import requests
import torch
from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def score_profile_image(url: str):
    image = Image.open(requests.get(url, stream=True).raw)
    inputs = processor(text=["attractive", "boring", "fun", "cool", "professional"], images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)
    scores = probs.detach().numpy()[0]
    labels = ["attractive", "boring", "fun", "cool", "professional"]
    return {label: float(round(score, 3)) for label, score in zip(labels, scores)}