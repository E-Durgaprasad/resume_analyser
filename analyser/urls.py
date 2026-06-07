from django.urls import path
from .views import home
from .api_views import ResumeUploadAPIView

urlpatterns = [
    path('',home,name='home'),
    path('api/upload/',ResumeUploadAPIView.as_view(),name='resume-upload'),
]