import os
from io import BytesIO

import torch
from PIL import Image
from torchvision.transforms import v2 as transforms

from .model_classes import BeautyModelV2

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")



# Create base model and load pretrained model onto it
def create_and_load_model(model_path: str = "src/Backend/app/models/final_model.pth"):
    model = BeautyModelV2()
    model.name = "BeautyModelV2"
    print(f"[INFO] Created new {model.name} model.")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model weights not found at {model_path}")
    
    state_dict = torch.load(
        model_path,
        map_location=DEVICE,
        weights_only=True,
    )
    model.load_state_dict(state_dict)

    return model.to(DEVICE).eval()

# Preprocessing transformation pipeline
preprocess = transforms.Compose([
    transforms.Resize(160),
    transforms.CenterCrop(160),
    transforms.ToImage(),
    transforms.ToDtype(torch.float32, scale=True),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Rating function 
@torch.inference_mode()
def predict(img_bytes: bytes, model: torch.nn.Module) -> float:
    img = Image.open(BytesIO(img_bytes)).convert("RGB")
    tensor = preprocess(img).unsqueeze(0).to(DEVICE)
    return float(model(tensor).item())
