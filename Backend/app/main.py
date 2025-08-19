from fastapi import FastAPI, UploadFile, File, HTTPException
from .utils import predict, load_model

# loads the model
model = load_model()

app = FastAPI(title="Face Rate")


@app.get("/")
async def health():
    return {"status": "good"}

@app.info("/info")
async def info():
    return {"name": "face-rate", "description": "Rate API images of faces."}

@app.post("/upload")
async def upload(photo: UploadFile = File(...)):
    """Receive an image file and return the model's rating."""
    if not (photo.content_type and photo.content_type.startswith("image/")):
        raise HTTPException(status_code=400, detail="File must be an image.")

    img_bytes = await photo.read()
    rating = predict(img_bytes)
    return {"rating": rating}