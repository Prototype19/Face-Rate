import torch
from torch import nn
from facenet_pytorch import InceptionResnetV1

class BeautyModelV2(nn.Module):
    def __init__(self, hidden_units=256):
        super().__init__()

        self.back_bone = InceptionResnetV1(pretrained='vggface2')
        back_bone_output_features = self.back_bone.last_linear.out_features

        self.classification_block = nn.Sequential(
            nn.Linear(in_features=back_bone_output_features, out_features=hidden_units),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(in_features=hidden_units, out_features=hidden_units//2),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_units//2, 1),
            nn.Sigmoid())



    def forward(self, x):
        return self.classification_block(self.back_bone(x)) * 4 + 1 # Outputs rating 1-5

def create_BeautyModelV2():
    model = BeautyModelV2()

    model.name = "BeautyModelV2"
    print(f"[INFO] Created new {model.name} model.")
    return model