from django.contrib import admin
from django.contrib.auth.models import Permission, User
from django.contrib.auth.hashers import make_password
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import path
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import StudentHM, StudentAL, SchoolProfile
from .forms import CsvImportForm

import csv, io

def import_csv(file, model):
	csv_reader = csv.reader(file, delimiter=',')
	print(csv_reader)
	for l in csv_reader:
		print(l)
		user = User.objects.get(username=l[0])
		_, created = model.objects.update_or_create(school=user, ctg=l[1], rollno=l[2], regno=l[3], name=l[4], fname=l[5], dob=l[6], subj=l[7], fl=l[8], sl=l[9])
	return True	

class StudentHMAdmin(admin.ModelAdmin):
	search_fields = ['rollno']
	@method_decorator(staff_member_required)
	def import_hm(self, request):
		if request.method == 'POST':
			csv_file = request.FILES['csv_file'].read().decode('UTF-8')
			io_string = io.StringIO(csv_file)
			csv = import_csv(io_string, self.model)
			messages.success(request, "Your csv file has been imported")
			return redirect(reverse("admin:%s_%s_changelist" %(self.model._meta.app_label, self.model._meta.model_name)))
		form = CsvImportForm()
		context = {"form": form}
		return render(request, "admin/csv_form.html", context)

	def get_urls(self):
		super_urls = super().get_urls()
		urls = [
			path('import/hm/students/', self.admin_site.admin_view(self.import_hm), name='import_hm')
		]
		return urls + super_urls

class StudentALAdmin(admin.ModelAdmin):
	search_fields = ['rollno']
	@method_decorator(staff_member_required)
	def import_al(self, request):
		if request.method == 'POST':
			csv_file = request.FILES['csv_file'].read().decode('UTF-8')
			io_string = io.StringIO(csv_file)
			csv = import_csv(io_string, self.model)
			messages.success(request, "Your csv file has been imported")
			return redirect(reverse("admin:%s_%s_changelist" %(self.model._meta.app_label, self.model._meta.model_name)))
		form = CsvImportForm()
		context = {"form": form}
		return render(request, "admin/csv_form.html", context)
		
	def get_urls(self):
		super_urls = super().get_urls()
		urls = [
			path('import/al/students/', self.admin_site.admin_view(self.import_al), name='import_al')
		]
		return urls + super_urls

class SchoolProfileAdmin(admin.ModelAdmin):
	search_fields = ['school__username']
	@method_decorator(staff_member_required)
	def reset_password(self, request, pk):
		profile = SchoolProfile.objects.get(pk=pk)
		user = profile.school
		user.password = make_password('password')
		user.save()

		update_permission = Permission.objects.get(codename='can_update')
		password_change_permission = Permission.objects.get(codename='can_change_password')
		user.user_permissions.remove(update_permission)
		user.user_permissions.add(password_change_permission)

		messages.success(request, f"Password of the school with index {user.username} has been reset to 'password'.")
		return redirect(reverse("admin:%s_%s_change" %(self.model._meta.app_label, self.model._meta.model_name), args=(pk,)))

	def get_urls(self):
		super_urls = super().get_urls()
		urls = [
			path('<int:pk>/reset-password/', self.admin_site.admin_view(self.reset_password), name='reset_password')
		]
		return urls + super_urls

admin.site.register(StudentHM, StudentHMAdmin)
admin.site.register(StudentAL, StudentALAdmin)
admin.site.register(SchoolProfile, SchoolProfileAdmin)