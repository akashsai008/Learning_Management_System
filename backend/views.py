from django.contrib.admin.views.decorators import user_passes_test
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomAdminForm
from .models import *
import firebase_admin
#from firebase_admin import credentials, storage
# Create your views here.

## cred = credentials.Certificate("D:\\project_backend\\backend_app\\resources\\svec-lms-firebase-adminsdk-m7ljj-471ebd201c.json") 
##firebase_admin.initialize_app(cred, {
## 'storageBucket': 'svec-lms.appspot.com'
###}) 

def add_video(request):
    form = CustomAdminForm(request.POST, request.FILES)
    if request.method=='POST':
        if form.is_valid():
            video_file = request.FILES['video']
            dept_id = form.cleaned_data['department']
            course_name = form.cleaned_data['course']
            description = request.POST['description']
            if dept_id is None or course_name is None or description is None:
                return HttpResponse("Missing POST data.")

        try:
            course = Course.objects.get(course_name=course_name)
        except Course.DoesNotExist:
            # Create a new course if it doesn't exist in the database
            course = Course.objects.create(course_name=course_name)  # Adjust as per your Course model

        # Define the folder path for the course
        course_folder = f"videos/{course.course_name}/"  # Assuming course.name is the folder name

        # Check if the folder exists in Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob(course_folder)  # Create a blob for the folder
        if not blob.exists():  # Check if the folder already exists
            blob.upload_from_string('')  # Create an empty folder

        bucket = storage.bucket()
        # Create a blob for the video file
        video_blob = bucket.blob(course_folder + video_file.name)
        # Upload the video file to Firebase Storage
        video_blob.upload_from_file(video_file, content_type=video_file.content_type)

        video_blob.make_public()
        # Get the public URL of the uploaded video
        public_url=video_blob.public_url

        s = Video(video_url=public_url,title=video_file.name,dept=Department.objects.get(dept=dept_id),course_name=Course.objects.get(course_name=course_name),description=description)
        s.save()
        return redirect('admin/backend/video/')
    return render(request,'upload.html',{'form': form})


def custom_action_view(request):
    return HttpResponse("Custom button clicked!")




