from fastapi import FastAPI, UploadFile, File, HTTPException
from utils import predict
import uvicorn

app = FastAPI(title="Face Rate")

@app.get("/")
async def status():
    return {"status": "ok"}

async def classify_image(file: UploadFile = File(...)):
    if file.content_type.split("/")[0] != "image":
        raise HTTPException(status_code=415, detail="Unsupported file type")

    img_bytes = await file.read()
    result    = predict(img_bytes)
    return {"filename": file.filename, "rating": result}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000)