from django.urls import path
from . import views
from post.views import index, meet, posting, new_post, remove_post

from django.conf.urls.static import static
from django.conf import settings

# app_name='post'
urlpatterns = [
    # 메인
    path('planpeak', views.index, name='index'),
    # 목록
    path('planpeak/post/global_search/', meet, name='meet'),
    # 모임소개
    path('planpeak/main/content/<int:pk>/',posting, name="posting"), 
    # 모임글 생성
    path('planpeak/post/content_save/', new_post),
    # 모임글 삭제
    path('planpeak/post/<int:pk>/content_delete/', remove_post),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)