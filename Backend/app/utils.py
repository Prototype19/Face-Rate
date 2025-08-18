import os
from io import BytesIO

import torch
from PIL import Image
from torchvision.transforms import v2 as transforms

from .model_classes import BeautyModelV2

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")



# Functions to create a model with the correct architecture
def create_model():
    model = BeautyModelV2()

    model.name = "BeautyModelV2"
    print(f"[INFO] Created new {model.name} model.")
    return model



# Load the model
def load_model(model_path: str = "models/final_model.pth"):
    model = create_model()
    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path, weights_only=True))
    model.eval()
    return model.to(DEVICE)

# Preprocessing transformation pipeline
preprocess = transforms.Compose([
    transforms.Resize(160),
    transforms.CenterCrop(160),
    transforms.ToImage(),
    transforms.ToDtype(torch.float32, scale=True),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Create a model
model = load_model()

# Convert image file into tensor
def bytes_to_tensor(data: bytes) -> torch.Tensor:
    img = Image.open(BytesIO(data)).convert("RGB")
    return preprocess(img).unsqueeze(0).to(DEVICE)

# Prediction function
@torch.inference_mode()
def predict(img_bytes: bytes) -> dict:
    x = bytes_to_tensor(img_bytes)
    prediction = model(x).item()
    return float(prediction)
