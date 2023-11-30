# "api_key": "####"
import numpy as np
from google.cloud import vision
import cv2

def detect_face(face_file, max_results = 10):
    client = vision.ImageAnnotatorClient(
        client_options={"api_key": "#####"}
    )
    content = face_file.read()
    image = vision.Image(content=content)
    responses = client.face_detection(image=image, max_results=max_results)
    return responses.face_annotations

def show_face(imagefile, faces, output_filename):
    img = cv2.imread(imagefile)
    for face in faces:
        box = [(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices]
        print(f'{box=}')
        cv2.polylines(img, [np.array(box)], True, (255,0,0), 2)
        print(f'{face.detection_confidence=}')
        cv2.putText(img, str(face.detection_confidence),
                    (face.fd_bounding_poly.vertices[0].x,
                     face.fd_bounding_poly.vertices[0].y-20),
                    cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255))

    for face in faces:
        box = [(vertex.x, vertex.y) for vertex in face.fd_bounding_poly.vertices]
        print(f'{box=}')
        cv2.polylines(img, [np.array(box)], True, (255, 255, 0), 2)

    cv2.imshow("IMG", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

input_filename="./img/children.jpg"
output_filename ="./googleoutp.jpg"
with open(input_filename, "rb") as image:
    faces = detect_face(image, 10)
    print(f'Found {len(faces)} face')
    show_face(input_filename, faces, output_filename)
    image = cv2.imread(input_filename)
    cv2.imshow("IMG", image)
