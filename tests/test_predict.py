import io
import pytest
from PIL import Image
import torch
import Backend.app.utils as utils

class DummyModel:
    def __call__(self, tensor):
        return torch.tensor([3.0])  

def test_predict_returns_expected_float(monkeypatch):

    monkeypatch.setattr(utils, "model", DummyModel())

    img = Image.new("RGB", (160, 160), color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")

    rating = utils.predict(buf.getvalue())

    assert isinstance(rating, float)
    assert rating == pytest.approx(3.0)

