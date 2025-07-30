import json, torch
from torchvision import transforms
from PIL import Image
from io import BytesIO
import model_classes

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")



# Functions to create a model with the correct architecture
def create_model():
    model = model_classes.BeautyModelV2()

    model.name = "BeautyModelV2"
    print(f"[INFO] Created new {model.name} model.")
    return model

# Create a model
model = create_model()

# Load the model
def load_model(model_path: str = "models/final_model.pth"):
    model = create_model()
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

# Convert image file into tensor
def bytes_to_tensor(data: bytes) -> torch.Tensor:
    img = Image.open(BytesIO(data)).convert("RGB")
    return preprocess.unsqueeze(0).to(DEVICE)

# Prediction function
@torch.inference_mode()
def predict(img_bytes: bytes) -> dict:
    x = bytes_to_tensor(img_bytes)
    prediction = model(x).item()
    return prediction