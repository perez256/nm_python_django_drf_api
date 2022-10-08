from django.urls import path

from common.control.authenticate import RegisterAPIView, LoginAPIView, UserAPIView, LogoutAPIView, ProfileAPIView, \
    ProfilePasswordAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('user', UserAPIView.as_view(), name='user'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('users/info', ProfileAPIView.as_view(), name='info'),
    path('users/password', ProfilePasswordAPIView.as_view(), name='password'),
]
