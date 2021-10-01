from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from student.camera import VideoCamera, FaceDetect, StudentEyeCatch
import cv2
import threading
import face_recognition
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST
from .models import EyeCal
def index(request):
    return render(request, 'index.html')

def prof_room(request):
    return render(request, 'prof_room.html')

def cam_capture(request):
    return render(request, 'cam_capture.html') 

def exam(request):
    return render(request, 'exam.html') 

def result(request):
    return render(request, 'result.html')   

def webrtc(request):
    return render(request, 'webrtc_server_client/rtc.html')

@require_POST
def home(request):
    # POST 요청일 때
    if request.method == 'POST':
        data = json.loads(request.body)
        # do something
        print(data)

        context = {
            'result': data,
        }
        return JsonResponse(context)


def gen(camera):
    while True:
        _, frame = FaceDetect().video.read()
        e = camera.faceRecognition(frame)
        _, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        # print('캡쳐했습니다.')
        # print('fhgfghfhg',frame)    # cv2.imwrite('dong.jpg', frame)
        # face_locations = face_recognition.face_locations(frame)
        # print('fhgfghfhg',frame)
        # dong_encoding = face_recognition.face_encodings(frame, face_locations)[0]
        #     # dong_image = face_recognition.load_image_file("dong.jpg")
        #     # dong_encoding = face_recognition.face_encodings(dong_image)[0]
        # print(e)
        if len(e) != 0:
            break


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
        # print('1')
        _, image = camera.video.read()
        frame = camera.func2(known_face_encodings,known_face_names,image)
        _, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def face_recog(request):
	return StreamingHttpResponse(gen(FaceDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def gen_video(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def eye_cap(request):
    while True:
        # print('1')
        ret, frame = StudentEyeCatch().video.read()
        if ret:
            cv2.imshow('camera-recording', frame)

            if cv2.waitKey(1) != -1:
                break
            # result = StudentEyeCatch().eyeCatch(frame)
            # print('asdf',frame)
            # print(result)
            # if result:
            #     break
            # _, jpeg = cv2.imencode('.jpg', frame)
            # frame = jpeg.tobytes()
            # yield (b'--frame\r\n'
            #         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            print('zoqdksehla')

def capture_face(request):
    return StreamingHttpResponse(eye_cap(request),
					content_type='multipart/x-mixed-replace; boundary=frame')

def exam_camera(camera):
        return StreamingHttpResponse(gen_video(VideoCamera()),
					content_type='multipart/x-mixed-replace; boundary=frame')