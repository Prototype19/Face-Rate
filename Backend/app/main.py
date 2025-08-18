from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .utils import predict 

app = FastAPI(title="Face Rate")

# Allow requests from any origin so the frontend can talk to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health():
    return {"status": "good"}


@app.post("/upload")
async def upload(photo: UploadFile = File(...)):
    """Receive an image file and return the model's rating."""
    if not (photo.content_type and photo.content_type.startswith("image/")):
        raise HTTPException(status_code=400, detail="File must be an image.")

    img_bytes = await photo.read()
    rating = predict(img_bytes)
    return {"rating": rating}