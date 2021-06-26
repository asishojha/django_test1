from django.shortcuts import redirect
from django import forms
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from formtools.preview import FormPreview
from .models import StudentHM, StudentAL
# from .decorators import has_update_permission

decorators = [login_required]

@method_decorator(decorators, name='__call__')
class StudentHMFormPreview(FormPreview):
	student = None
	next_student = None
	form_template = 'mdmarks/student.html'
	preview_template = 'mdmarks/preview.html'

	def parse_params(self, request, *args, **kwargs):
		try:
			self.student = StudentHM.objects.get(school=request.user, rollno=kwargs['rollno'])
		except StudentHM.DoesNotExist:
			self.student = None

		try:
			self.next_student = StudentHM.objects.filter(school=request.user, complete=False).exclude(rollno=kwargs['rollno']).order_by('rollno')[0]
		except IndexError:
			self.next_student = None

	def get_initial(self, request):
		student_dict = model_to_dict(self.student, fields=[field.name for field in self.student._meta.fields])
		return student_dict

	def get_context(self, request, form):
		students = StudentHM.objects.filter(school=request.user).order_by('rollno')
		return {
			'form': form,
			'stage_field': self.unused_name('stage'),
			'state': self.state,
			'students': students,
			'student': self.student,
		}

	def done(self, request, cleaned_data):
		self.student.fl_marks = cleaned_data.get('fl_marks')
		self.student.english_marks = cleaned_data.get('english_marks')
		self.student.maths_marks = cleaned_data.get('maths_marks')
		self.student.psc_marks = cleaned_data.get('psc_marks')
		self.student.lsc_marks = cleaned_data.get('lsc_marks')
		self.student.hist_marks = cleaned_data.get('hist_marks')
		self.student.geog_marks = cleaned_data.get('geog_marks')
		self.student.arabic_marks = cleaned_data.get('arabic_marks')
		self.student.opt_marks = cleaned_data.get('opt_marks')
		self.student.islam_parichay = cleaned_data.get('islam_parichay')
		self.student.complete=True
		self.student.save()
		if self.next_student is not None:
			messages.success(request, f'Congratulations! Data for student {self.student.rollno} has been updated.')
			return redirect(self.next_student.get_absolute_url())
		else:
			messages.success(request, 'Congratulations! Data for all the students have been updated.')
			return redirect('mdmarks:students')

	def __call__(self, request, *args, **kwargs):
		return super(StudentHMFormPreview, self).__call__(request, *args, **kwargs)

@method_decorator(decorators, name='__call__')
class StudentALFormPreview(FormPreview):
	student = None
	next_student = None
	form_template = 'mdmarks/student.html'
	preview_template = 'mdmarks/preview.html'

	def parse_params(self, request, *args, **kwargs):
		try:
			self.student = StudentAL.objects.get(school=request.user, rollno=kwargs['rollno'])
		except StudentAL.DoesNotExist:
			self.student = None

		try:
			self.next_student = StudentAL.objects.filter(school=request.user, complete=False).exclude(rollno=kwargs['rollno']).order_by('rollno')[0]
		except IndexError:
			self.next_student = None

	def get_initial(self, request):
		student_dict = model_to_dict(self.student, fields=[field.name for field in self.student._meta.fields])
		return student_dict

	def get_context(self, request, form):
		students = StudentAL.objects.filter(school=request.user).order_by('rollno')
		return {
			'form': form,
			'stage_field': self.unused_name('stage'),
			'state': self.state,
			'students': students,
			'student': self.student,
		}

	def done(self, request, cleaned_data):
		self.student.fl_marks = cleaned_data.get('fl_marks')
		self.student.english_marks = cleaned_data.get('english_marks')
		self.student.maths_marks = cleaned_data.get('maths_marks')
		self.student.psc_marks = cleaned_data.get('psc_marks')
		self.student.lsc_marks = cleaned_data.get('lsc_marks')
		self.student.hist_marks = cleaned_data.get('hist_marks')
		self.student.geog_marks = cleaned_data.get('geog_marks')
		self.student.arabic_marks = cleaned_data.get('arabic_marks')
		self.student.opt_marks = cleaned_data.get('opt_marks')
		self.student.hadith = cleaned_data.get('hadith')
		self.student.tafsir = cleaned_data.get('tafsir')
		self.student.fiqh = cleaned_data.get('fiqh')
		self.student.complete=True
		self.student.save()
		if self.next_student is not None:
			messages.success(request, f'Congratulations! Data for student {self.student.rollno} has been updated.')
			return redirect(self.next_student.get_absolute_url())
		else:
			messages.success(request, 'Congratulations! Data for all the students have been updated.')
			return redirect('mdmarks:students')

	def __call__(self, request, *args, **kwargs):
		return super(StudentALFormPreview, self).__call__(request, *args, **kwargs)