from django.urls import path
from .views import index, login, logout, school_profile, reset_password, students
from .previews import StudentHMFormPreview, StudentALFormPreview
from .forms import StudentHMForm, StudentALForm

app_name = 'mdmarks'

urlpatterns = [
	path('', index, name='index'),
	path('login/', login, name='login'),
	path('logout/', logout, name='logout'),
	path('update-school-profile/', school_profile, name='profile'),
	path('reset-password/', reset_password, name='reset_password'),
	path('students/', students, name='students'),
	path('student/hm/<slug:rollno>/', StudentHMFormPreview(StudentHMForm), name='student_hm'),
	path('student/al/<slug:rollno>/', StudentALFormPreview(StudentALForm), name='student_al'),
]