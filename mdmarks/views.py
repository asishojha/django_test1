from django.shortcuts import render, redirect
from django.contrib.auth import login as user_login, logout as user_logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.admin.views.decorators import staff_member_required

from .models import SchoolProfile, StudentAL, StudentHM
from .forms import UsersLoginForm, SchoolProfileForm, PasswordResetForm, CsvImportForm
import csv, io

def index(request):
	return render(request, 'mdmarks/index.html')

def login(request):
	if request.user.is_authenticated:
		return redirect('mdmarks:index')

	form = UsersLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username = username, password = password)
		user_login(request, user)
		ct = ContentType.objects.get_for_model(User)
		permission_change_password, created_change_password = Permission.objects.get_or_create(codename='can_change_password', name='Can change the password', content_type=ct)
		permission_update_data, created_update_data = Permission.objects.get_or_create(codename='can_update', name='Can Update the database of students', content_type=ct)
		if user.has_perm('auth.can_update'):		
			return redirect('mdmarks:students')
		try:
			profile = user.schoolprofile
			if not user.has_perm('auth.can_change_password'):
				return redirect('mdmarks:students')
			return redirect('mdmarks:reset_password')
		except SchoolProfile.DoesNotExist:
			return redirect('mdmarks:profile')
	context = {
		'form': form
	}
	return render(request, 'mdmarks/accounts/login.html', context)

@login_required
def logout(request):
	user_logout(request)
	return redirect('mdmarks:index')

@login_required
def school_profile(request):
	user = request.user
	try:
		profile = user.schoolprofile
		if not user.has_perm('auth.can_change_password'):
			return redirect('mdmarks:students')
		else:
			return redirect('mdmarks:reset_password')
	except SchoolProfile.DoesNotExist:
		pass

	form = SchoolProfileForm()
	if request.method == 'POST':
		form = SchoolProfileForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.school = user
			profile.save()
			user.email = profile.email
			user.save()
			permission = Permission.objects.get(codename='can_change_password')
			user.user_permissions.add(permission)
			return redirect('mdmarks:reset_password')
	context = {
		'form': form
	}
	return render(request, 'mdmarks/school-profile.html', context)

@login_required
def reset_password(request):
	if not request.user.has_perm('auth.can_change_password'):
		try:
			profile = request.user.schoolprofile
			return redirect('mdmarks:students')
		except SchoolProfile.DoesNotExist:
			return redirect('mdmarks:profile')

	form = PasswordResetForm(request.user)
	update_permission = Permission.objects.get(codename='can_update')
	password_change_permission = Permission.objects.get(codename='can_change_password')
	if request.method == 'POST':
		form = PasswordResetForm(request.user, request.POST)
		if form.is_valid():
			password = form.save()
			update_session_auth_hash(request, password)
			if not request.user.has_perm('auth.can_update'):
				request.user.user_permissions.add(update_permission)
			request.user.user_permissions.remove(password_change_permission)
			messages.success(request, 'Password Changed Successfully!')
			return redirect('mdmarks:students')
	context = {
		'form': form
	}
	return render(request, 'mdmarks/accounts/reset-password.html', context)

@login_required
def students(request):
	if not request.user.has_perm('auth.can_update'):
		return redirect('mdmarks:reset_password')

	Student = StudentHM
	students = Student.objects.filter(school=request.user).order_by('rollno')
	if students.count() == 0:
		Student = StudentAL
		students = Student.objects.filter(school=request.user).order_by('rollno')

	ctg = students[0].ctg
	if list(ctg)[0] == '1':
		school_type = 'HIGH MADRASAH'
	elif list(ctg)[0] == '3':
		school_type = 'ALIM'

	paginator = Paginator(students,15)
	page = request.GET.get('page',1)

	try:
		first_student = students.filter(complete=False)[0]
	except (Student.DoesNotExist, IndexError):
		first_student = None

	try:
		students = paginator.page(page)
	except PageNotAnInteger:
		students = paginator.page(1)
	except EmptyPage:
		students = paginator.page(paginator.num_pages)	

	context = {
		'students': students,
		'first_student': first_student,
		'regular' : Student.objects.filter(school=request.user , ctg__endswith='1').count(),
		'continuity' : Student.objects.filter(school=request.user , ctg__endswith='3').count(),
		'compartmental' : Student.objects.filter(school=request.user , ctg__endswith='5').count(),
		'tot' : Student.objects.filter(school=request.user).count(),
		'left' : Student.objects.filter(school=request.user, complete=False).count(),
		'done' : Student.objects.filter(school=request.user, complete=True).count(),
		'school_type': school_type
	}
	return render(request, 'mdmarks/students.html', context)

@staff_member_required
def import_users(request):
	form = CsvImportForm()
	if request.method == 'POST':
		csv_file = request.FILES['csv_file'].read().decode('UTF-8')
		io_string = io.StringIO(csv_file)
		csv_reader = csv.reader(io_string, delimiter=',')
		for l in csv_reader:
			User.objects.create_user(username=l[0], first_name=l[1], password='password')
		messages.success(request, "Your csv file has been imported")
		return redirect(reverse("admin:auth_user_changelist"))
	context = {"form": form}
	
	return render(request, "admin/csv_form.html", context)

def instructions(request):
	return render(request, 'mdmarks/instructions.html')

@staff_member_required
def admin_info(request):
	complete_hm_students = StudentHM.objects.filter(complete=True).count()
	complete_al_students = StudentAL.objects.filter(complete=True).count()
	no_of_profiles = SchoolProfile.objects.all().count()
	incomplete_schools = []
	schools = User.objects.exclude(is_superuser=True)

	for s in schools:
		hm_students = s.studenthm_set.all()
		al_students = s.studental_set.all()

		if hm_students.count() > 0:
			try:
				inc_student = hm_students.get(complete=True)
			except MultipleObjectsReturned:
				pass
			except StudentHM.DoesNotExist:
				incomplete_schools.append(s)

		if al_students.count() > 0:
			try:
				inc_student = al_students.get(complete=True)
			except MultipleObjectsReturned:
				pass
			except StudentAL.DoesNotExist:
				incomplete_schools.append(s)


	context = {
		'complete_hm_students': complete_hm_students,
		'complete_al_students': complete_al_students,
		'no_of_profiles': no_of_profiles,
		'incomplete_schools': incomplete_schools
	}
	return render(request, 'admin-info.html', context)