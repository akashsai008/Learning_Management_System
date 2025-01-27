from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import HttpResponse,response
from .forms import *
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from backend.models import *
# Create your views here.
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import StudentIDLoginForm

def login(request):
    if request.method == 'POST':
        form = StudentIDLoginForm(request.POST)
        if form.is_valid():
            rollnumber = form.cleaned_data.get('rollnumber')
            password = form.cleaned_data.get('password')
            user = authenticate(request, rollno=rollnumber, password=password)  # Use rollnumber for authentication
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid roll number or password")
    else:
        form = StudentIDLoginForm()

    return render(request, 'frontend/login.html', {'form': form})


def home(request):

    courses = Course.objects.prefetch_related('videos').all()
    departments = Department.objects.all()
    videos=Video.objects.all()
    context = {
        'courses': courses,
        'departments': departments,
        'videos':videos,
    }
    response = render(request, 'frontend/home_page.html', context)
    response.set_cookie('username', '22A81A05Q2')  # Lasts until browser is closed
    
    return render(request,'frontend/home_page.html',context)

def about(request):
    return render(request,'frontend/about.html')

def profile(request):
    # username = request.COOKIES.get('username')
    # return HttpResponse(username)
    return render(request,'frontend/profile.html')

def course_details(request,course_name):
    videos = Video.objects.all()
    return render(request,'frontend/fetch_course_videos.html',{'videos':videos})

def fetch_course_videos(request,course_name):
    course = Course.objects.get(course_name=course_name)
    # Filter videos based on the selected department and course
    get_course = get_object_or_404(Course, course_name=course_name)
    
    # Filter videos related to the selected course using the correct relationship
    videos = Video.objects.filter(course_name=get_course) 
    # Filtering by selected course
    #current_url = Video.objects.get(title=course_name)
    context = {
        'videos': videos,
        'course': course,
        'title':course_name,

    }

    return render(request, 'frontend/fetch_course_videos.html', context)

def verifypassword(request):
    form = StudentIDLoginForm()
    if request.method=='POST':
        form = StudentIDLoginForm(request.POST)
        old_password = request.POST['password']
        # username = form.POST['old_password']   
        if form.is_valid(): 
            try:
                user = authenticate(request,rollno='22A81A05Q2',password=old_password)

                if user is not None:  # Check if the old password is correct
                    return HttpResponse("Old password is correct!")
                else:
                    return HttpResponse("Old password is incorrect.")
            except Lms_Users.DoesNotExist:
                return HttpResponse("User does not exist.")

    return render(request, 'frontend/verifypassword.html',{'form':form})