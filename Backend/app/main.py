from fastapi import FastAPI, UploadFile, File, HTTPException
from .utils import predict, create_and_load_model

# loads the model
model = create_and_load_model()

app = FastAPI(title="Face Rate")


@app.get("/")
async def health():
    return {"status": "good"}

@app.get("/info")
async def info():
    return {"name": "face-rate", "description": "Rate API images of faces."}

@app.post("/upload")
async def upload(photo: UploadFile = File(...)):
    if not (photo.content_type and photo.content_type.startswith("image/")):
        raise HTTPException(status_code=400, detail="File must be an image.")

    img_bytes = await photo.read()
    rating = predict(img_bytes, model)

    return {"rating": rating}