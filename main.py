from fastapi import FastAPI, File, UploadFile

import pytesseract
from PIL import Image

from .routers import users

app = FastAPI()

# Routes
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Cannot GET, send image file in the post method"}


@app.post("/")
async def image_to_text(file: UploadFile = File(...)):
    if file:
        img = Image.open(file)
        text = pytesseract.image_to_string(img)
        return {"content": text}
    else:
        return {"message": "please send image file"}
