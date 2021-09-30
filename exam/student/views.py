from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from student.camera import VideoCamera, FaceDetect
import cv2
import threading
import face_recognition
def index(request):
    return render(request, 'index.html')

def webrtc(request):
    return render(request, 'webrtc_server_client/rtc.html')

def gen(camera):
    while True:
        _, frame = FaceDetect().video.read()
        e = camera.faceRecognition(frame)
        # print('캡쳐했습니다.')
        # print('fhgfghfhg',frame)    # cv2.imwrite('dong.jpg', frame)
        # face_locations = face_recognition.face_locations(frame)
        # print('fhgfghfhg',frame)
        # dong_encoding = face_recognition.face_encodings(frame, face_locations)[0]
        #     # dong_image = face_recognition.load_image_file("dong.jpg")
        #     # dong_encoding = face_recognition.face_encodings(dong_image)[0]
        if e is not None:
            break

    print('break ehoTtmqslek')
    # image = FaceDetect().video.read()
    # e = camera.faceRecognition(image)
    known_face_encodings = [
            e,
            # obama_face_encoding,
            # biden_face_encoding
        ]
    known_face_names = [
            "Dong",
            # "Barack Obama",
            # "Joe Biden"
    ]
    while True:
        print('1')
        _, image = FaceDetect().video.read()
        frame = FaceDetect().func2(known_face_encodings,known_face_names,image)
        _, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def face_recog(request):
	return StreamingHttpResponse(gen(FaceDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')