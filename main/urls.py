from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('validatePost/', views.validatePost, name='validatePost'),
    path('validatePostById/<str:id>', views.validatePostById, name='validatePostById'),
    path('requestSupervisor/<str:id>', views.requestSupervisor, name='requestSupervisor'),
    path('supreq/', views.allReqSup, name='supreq'),
    path('newpost/', views.newpost, name='newpost'),
    path('getPremium/', views.getPremium, name='getPremium'),
    path('makesup/<str:id>', views.makesup, name='makesup'),
]
