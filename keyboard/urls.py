from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('keyboardname/', views.keyboardname, name='keyboardname'),
    path('keyboardimage/', views.keyboardimage, name='keyboardimage'),
    path('keyboardDetail/<int:id>', views.keyboardDetail, name='detail'),
    path('newkeyboard/', views.newKeyboard, name='newkeyboard'),
    path('newkeyboardimage/', views.newKeyboardImage, name='newkeyboardimage'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
