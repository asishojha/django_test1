from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth.hashers import make_password
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import path
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from .models import StudentHM, StudentAL, SchoolProfile

class StudentHMAdmin(admin.ModelAdmin):
	search_fields = ['rollno']

class StudentALAdmin(admin.ModelAdmin):
	search_fields = ['rollno']

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