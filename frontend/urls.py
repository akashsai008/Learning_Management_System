from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='loginpage'),
    path('home/',views.home,name='home'),
    #path('course/<str:title>', views.fetch_course_videos, name='fetch_course_videos'),
    path('course/<str:course_name>', views.fetch_course_videos, name='fetch_course_videos'),
    path('about/',views.about,name='about'),
    path('profile/',views.profile,name='profile'),
    path('verifypassword/',views.verifypassword,name='verifypassword'),
    path('course_details/<str:course_name>',views.course_details,name='course_details'),
]
