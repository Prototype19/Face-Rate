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

# Load the model
def load_model(model_path: str = "models/final_model.pth"):
    model = create_model()
    model.load_state_dict(torch.load(model_path, weights_only=True))
    # set model into eval mode 
    model.eval()
    return model

# Create predict function