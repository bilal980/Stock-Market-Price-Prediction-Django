from django.urls import path
from . import views

urlpatterns = [
    path('', views.foxBlog),
    path('postcomment/', views.comment_post),
    path('<str:slug>/', views.foxdetailpost, name='detailpost')
]
