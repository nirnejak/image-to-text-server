from fastapi import FastAPI, File, UploadFile

import pytesseract
from PIL import Image

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Cannot GET, send image file in the post method" }

@app.post("/")
async def image_url(file: UploadFile = File(...)):
    if file:
        img = Image.open(file)
        text = pytesseract.image_to_string(img)
        return { "content": text }
    else:
        return { "message": "please send image_url" }
