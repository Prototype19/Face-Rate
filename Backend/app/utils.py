import json, torch
from torchvision import transforms
from PIL import Image
from io import BytesIO

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")





# Function to create the model with the correct architecture
def create_model():
    return None
# Load the model
def load_model(model_path: str = "models/final_model.pth"):
    return None