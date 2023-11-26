from fastapi import FastAPI, WebSocket
import base64
import cv2
import numpy as np
import torch
from preprocess import image_decode

app = FastAPI()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # 클라이언트로부터 Base64 인코딩된 이미지를 받습니다
            base64_string = await websocket.receive_text()

            # Base64 문자열을 이미지로 디코딩합니다
            image_bytes = base64.b64decode(base64_string)
            image = image_decode(image_bytes)

            # 이미지를 그레이스케일로 변환합니다.
            gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # 얼굴 탐지를 수행합니다.
            faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            if len(faces) == 0:
                await websocket.send_text(f"No face in image")
            # 얼굴 부분을 크롭하고 저장합니다.
            for (x, y, w, h) in faces:
                # 얼굴 부분을 크롭합니다.
                cropped_face = image[y:y+h, x:x+w]

                # 결과를 클라이언트에게 보냅니다
                await websocket.send_text(f"Detection Results: str({cropped_face.shape})")

    except Exception as e:
        print(f"Error: {e}")
        await websocket.send_text(f"Error: {e}")
    finally:
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="yolo-server:app", host="0.0.0.0", port=65502, reload=True)