from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('prof_room',views.prof_room, name="prof_room"),
    path('cam_capture',views.cam_capture, name="cam_capture"),
    path('face',views.face_recog, name="face"),
    path('result',views.result, name="result"),
    path('exam',views.exam, name="exam"),
    path('webrtc', views.webrtc, name="webrtc"),
    path('eyecapture',views.capture_face, name="eyecapture"),
    path('exam_camera',views.exam_camera, name="exam_camera"),
]