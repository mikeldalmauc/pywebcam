import os
import cv2
import uuid
from dotenv import load_dotenv
from pathlib import Path
import time

# Inicialización

## Cargar variables de entorno como la ip de la cámara
dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)

CAMERA_IP = os.getenv('CAMERA_IP')
CAMERA_PORT = os.getenv('CAMERA_PORT')

## Inicilizar el clasificador de caras
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

## directorio de salida
outputdir='../output/'

## Inicializar la cámara
video_capture = cv2.VideoCapture('http://'+CAMERA_IP+':'+CAMERA_PORT+'/mjpeg')

# Definir algunas funciones que se utilizarán en el bucle principal

## esta función detecta una cara y devuelve las coordenadas de los BoundingBox de las caras detectadas
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(60, 60))
    return faces


## esta función pinta un rectangulo para cada cara
def paint_bounding_box(vid, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return True

## esta función escribe las caras detectadas en el directorio de salida
def write_faces(vid, faces):
    for (x, y, w, h) in faces:
        cv2.imwrite(outputdir+'face-'+str(uuid.uuid4())+'.jpg', vid[y:y+h, x:x+w])
    return True
         

# Bucle principal

while True:
    
    # Leer los frames de la cámara
    result, video_frame = video_capture.read()  
    if result is False:
        break  

    # Detectar las caras
    faces = detect_bounding_box(video_frame) 
    print(faces)

    # Guardar las caras
    write_faces(video_frame, faces)
    
    time.sleep(0.5)

video_capture.release()
cv2.destroyAllWindows()