from fastapi import FastAPI, UploadFile, File, HTTPException
from utils import predict


app = FastAPI(title="Face Rate")

@app.get("/")
async def health():
    return {"status": "good"}