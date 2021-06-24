from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm

from .models import SchoolProfile, StudentHM, StudentAL

SUBJECT_CODE_DICT = {
	'001': 'BENGALI',
	'002': 'URDU',
	'017': 'BIOLOGY',
	'021': 'ISLAMIC HISTORY',
	'022': 'WORK/PHY. EDU.',
	'087': 'MCA',
	'057': 'BENGALI',
	'058': 'URDU',
	'085': 'BIOLOGY',
	'135': 'FARAID'
}

class PasswordResetForm(PasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super(PasswordChangeForm, self).__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})

class UsersLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
	
	def __init__(self, *args, **kwargs):
		super(UsersLoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
			'class': 'form-control',
			'name':'username'})
		self.fields['password'].widget.attrs.update({
			'class': 'form-control',
			'name':'password'})

	def clean(self, *args, **keyargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		if username and password:
			user = authenticate(username = username, password = password)
			if not user:
				raise forms.ValidationError('Invalid Credentials! Please check username and password again.')
			if not user.is_active:
				raise forms.ValidationError('User is no longer active')

class SchoolProfileForm(forms.ModelForm):
	class Meta:
		model = SchoolProfile
		exclude = ['school']     
	def __init__(self, *args, **kwargs):
		super(SchoolProfileForm, self).__init__(*args, **kwargs)
		
		self.fields['name'].label = 'Name of H.M. / T.I.C'      
		self.fields['phone'].label = 'Mobile Number'

		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control'})

class StudentHMForm(forms.ModelForm):
	class Meta:
		model = StudentHM
		fields = ['rollno', 'regno', 'name', 'fname', 'dob', 'subj', 'fl', 'sl', 'fl_marks', 'english_marks', 'maths_marks', 'psc_marks', 'lsc_marks', 'hist_marks', 'geog_marks', 'arabic_marks', 'islam_parichay', 'opt_marks']

	def __init__(self, *args, **kwargs):
		super(StudentHMForm, self).__init__(*args, **kwargs)
		if self['sl'].value():
			self.fields['opt_marks'].label = SUBJECT_CODE_DICT[self['sl'].value()].title()
		else:
			self.fields['sl'].required = False
			self.fields['opt_marks'].required = False
		self.fields['fl_marks'].label = SUBJECT_CODE_DICT[self['fl'].value()].title()
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control mb-3'})
			if self[field].value() is not None:
				self.fields[field].widget.attrs.update({'disabled': ''})
			if len(self[field].errors) > 0:
				print(self[field])
				self.fields[field].widget.attrs.pop('disabled')

class StudentALForm(forms.ModelForm):
	class Meta:
		model = StudentAL
		fields = ['rollno', 'regno', 'name', 'fname', 'dob', 'subj', 'fl', 'sl', 'fl_marks', 'english_marks', 'arabic_marks', 'hadith', 'tafsir', 'fiqh', 'maths_marks', 'psc_marks', 'lsc_marks', 'hist_marks', 'geog_marks', 'opt_marks']
		# exclude = ['complete','ctg']

	def __init__(self, *args, **kwargs):
		super(StudentALForm, self).__init__(*args, **kwargs)
		if self['sl'].value():
			self.fields['opt_marks'].label = SUBJECT_CODE_DICT[self['sl'].value()].title()
		else:
			self.fields['sl'].required = False
			self.fields['opt_marks'].required = False
		self.fields['fl_marks'].label = SUBJECT_CODE_DICT[self['fl'].value()].title()
		for field in self.fields:
			self.fields[field].widget.attrs.update({'class': 'form-control mb-3'})
			if self[field].value() is not None:
				self.fields[field].widget.attrs.update({'disabled': ''})
			if len(self[field].errors) > 0:
				print(self[field])
				self.fields[field].widget.attrs.pop('disabled')

class CsvImportForm(forms.Form):
	csv_file = forms.FileField()

	def __init__(self):
		super().__init__()
		self.fields['csv_file'].widget.attrs.update({'class':'vTextField', 'accept':'.csv'})