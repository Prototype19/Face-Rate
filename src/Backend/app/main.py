from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from .utils import predict, create_and_load_model

# loads the model
model = create_and_load_model()

BASE_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIR = BASE_DIR / "Frontend"

app = FastAPI(title="Face Rate")
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/")
async def index():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/health")
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