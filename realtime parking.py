import cv2
import pandas as pd
import numpy as np
from ultralytics import YOLO
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("D:\project\smart parking system\yolov8parkingspace-main\yolov8parkingspace-main\smart-parking-using-iot-8d52a-firebase-adminsdk-bjmax-433ab6cf73.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-parking-using-iot-8d52a-default-rtdb.firebaseio.com/'
})

ref = db.reference('/parking')

model = YOLO('yolov8s.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap = cv2.VideoCapture('parking1.mp4')

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")
   
areas = {
    'area1': [(52, 364), (30, 417), (73, 412), (88, 369)],
    'area2': [(105, 353), (86, 428), (137, 427), (146, 358)],
    'area3': [(159, 354), (150, 427), (204, 425), (203, 353)],
    'area4': [(217,352),(219,422),(273,418),(261,347)],
    'area5': [(274,345),(286,417),(338,415),(321,345)],
    'area6': [(336,343),(357,410),(409,408),(382,340)],
    'area7': [(396,338),(426,404),(479,399),(439,334)],
    'area8': [(458,333),(494,397),(543,390),(495,330)],
    'area9': [(511,327),(557,388),(603,383),(549,324)],
    'area10': [(564,323),(615,381),(654,372),(596,315)],
    'area11': [(616,316),(666,369),(703,363),(642,312)],
    'area12': [(674,311),(730,360),(764,355),(707,308)],
}

while True:
    ret, frame = cap.read()
    if not ret:
        break
    time.sleep(0)
    frame = cv2.resize(frame, (1020, 500))
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
    vacancies = {}
    for area_name, area_coords in areas.items():
        area_vacancies = 0
        for index, row in px.iterrows():
            x1, y1, x2, y2, _, class_id = row
            class_name = class_list[int(class_id)]
            if 'car' in class_name:
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)
                if cv2.pointPolygonTest(np.array(area_coords, np.int32), (cx, cy), False) >= 0:
                    area_vacancies += 1
        vacancies[area_name] = 1 if area_vacancies == 0 else 0 
    ref.update(vacancies)
    for area_name, area_coords in areas.items():
        color = (0, 255, 0) if vacancies[area_name] == 1 else (0, 0, 255) 
        cv2.polylines(frame, [np.array(area_coords, np.int32)], True, color, 2)
        cv2.putText(frame, "Vacant" if vacancies[area_name] == 1 else "Occupied", (area_coords[0][0], area_coords[0][1] - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)  # Display "Vacant" if vacant, otherwise "Occupied"
    
    cv2.imshow("RGB", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
