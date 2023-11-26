from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import io
import base64
from PIL import Image
import torch
import onnxruntime

import cv2
import numpy as np

from get_prompt import get_prompt
from ppe import ppe
from get_corrected_sentence import get_corrected_sentence
import uvicorn
import easyocr
from preprocess import preprocess
import requests

app = FastAPI()

class ImageData(BaseModel):
    imageUrl: str

reader = easyocr.Reader(['en'])

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/image-to-text")
async def detect_objects(data: ImageData):
    try:
        image_url = data.imageUrl
        response = requests.get(image_url)
        image_bytes = response.content

        #image = preprocess(image_bytes, 640, 640)

        output = reader.readtext(image_bytes, detail = 0, paragraph=True, decoder='wordbeamsearch', beamWidth=7)
        sentence = get_corrected_sentence(output)

        # 결과를 처리하고 반환합니다 (여기서는 예시로 단순히 결과의 문자열 표현을 반환합니다)
        return {"sentences": sentence}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app="server:app", host="0.0.0.0", port=65501)
