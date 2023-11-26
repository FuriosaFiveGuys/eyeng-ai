# from ultralytics import YOLO

# # Load a model
# model = YOLO('yolov8n.pt')  # load an official model
# print(model)
# # Export the model

# for s in model.state_dict():
#     print(s)

# onnx_file = model.export(format='onnx', dynamic=False, opset=13)


import cv2

# 이미지를 불러옵니다.
image_path = "./1.jpg"  # 이미지 파일 경로
img = cv2.imread(image_path)

# Haar Cascade 얼굴 탐지기를 불러옵니다.
# OpenCV에서 기본적으로 제공하는 사전 훈련된 모델을 사용합니다.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 이미지를 그레이스케일로 변환합니다.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 탐지를 수행합니다.
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 얼굴 부분을 크롭하고 저장합니다.
for (x, y, w, h) in faces:
    # 얼굴 부분을 크롭합니다.
    cropped_face = img[y:y+h, x:x+w]

    print(cropped_face.shape)
