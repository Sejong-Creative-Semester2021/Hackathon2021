from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('face',views.face_recog, name="face"),
    path('webrtc', views.webrtc, name="webrtc"),
]