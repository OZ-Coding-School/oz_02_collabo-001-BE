from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'), # 메일 폼 url
    path('send/', sendEmail),      # 메일 발송 처리 url
]