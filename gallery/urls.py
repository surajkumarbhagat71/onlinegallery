from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('addimage',InsertImage.as_view(),name="addimage"),
    path('login',Login.as_view(),name="login"),
    path('signup',Signup.as_view(),name="signup"),
    path('logout',Login.as_view(),name="logout"),
    path('myupload',MyUpload.as_view(),name="myupload"),
    path('delete/<int:pk>',DeleteMyImage.as_view(),name="deletemyupload"),
    path('about',About.as_view(),name="about"),
    path('viewimage/<int:pk>',ViewImage.as_view(),name="viewimage"),

]