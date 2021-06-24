from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

from .validators import validate_100_marks, validate_50_marks

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

CATEGORY_DICT = {
	'1': 'REGULAR',
	'3': 'CONTINUING',
	'5': 'COMPARTMENTAL'
}

class Student(models.Model):
	school = models.ForeignKey(User, on_delete=models.CASCADE)
	ctg = models.CharField(max_length=2)
	rollno = models.CharField(max_length=9, verbose_name='Roll-Number')
	regno = models.CharField(max_length=10, verbose_name='Registration Number')
	name = models.CharField(max_length=40, verbose_name='Name')
	fname = models.CharField(max_length=40, verbose_name='Father\'s Name')
	dob = models.CharField(max_length=8, verbose_name='Date of Birth')
	subj = models.CharField(max_length=40, null=True, verbose_name='Subject Combination')
	fl = models.CharField(max_length=3)
	sl = models.CharField(max_length=3, null=True)
	fl_marks = models.CharField(max_length=3, null=True, validators=[validate_100_marks])
	english_marks = models.CharField(max_length=3, null=True, verbose_name='English (SL)', validators=[validate_100_marks])
	maths_marks = models.CharField(max_length=3, null=True, verbose_name='Mathematics', validators=[validate_100_marks])
	arabic_marks = models.CharField(max_length=3, null=True, verbose_name='Arabic', validators=[validate_100_marks])
	hist_marks = models.CharField(max_length=3, null=True, verbose_name='History', validators=[validate_100_marks])
	opt_marks = models.CharField(max_length=3, null=True, validators=[validate_100_marks])
	complete=models.BooleanField(default=False)

	def get_fl_name(self):
		return SUBJECT_CODE_DICT[self.fl]

	def get_cateogry(self):
		return CATEGORY_DICT[list(self.ctg)[-1]]

	class Meta:
		abstract = True

class StudentHM(Student):
	islam_parichay = models.CharField(max_length=3, null=True, validators=[validate_100_marks])
	psc_marks = models.CharField(max_length=3, null=True, verbose_name='Physical Science', validators=[validate_100_marks])
	lsc_marks = models.CharField(max_length=3, null=True, verbose_name='Life Science', validators=[validate_100_marks])
	geog_marks = models.CharField(max_length=3, null=True, verbose_name='Geography', validators=[validate_100_marks])

	class Meta:
		verbose_name_plural = 'Students HM'

	def __str__(self):
		return f'{self.school.username} - {self.rollno}'

	def get_absolute_url(self):
		return reverse('mdmarks:student_hm', kwargs={
			'rollno': self.rollno	
		})

class StudentAL(Student):
	psc_marks = models.CharField(max_length=2, null=True, verbose_name='Physical Science', validators=[validate_50_marks])
	lsc_marks = models.CharField(max_length=2, null=True, verbose_name='Life Science', validators=[validate_50_marks])
	geog_marks = models.CharField(max_length=2, null=True, verbose_name='Geography', validators=[validate_50_marks])
	hadith = models.CharField(max_length=3, null=True, validators=[validate_100_marks])
	tafsir = models.CharField(max_length=3, null=True, validators=[validate_100_marks])
	fiqh = models.CharField(max_length=2, null=True, validators=[validate_50_marks])

	class Meta:
		verbose_name_plural = 'Students AL'

	def __str__(self):
		return f'{self.school.username} - {self.rollno}'

	def get_absolute_url(self):
		return reverse('mdmarks:student_al', kwargs={
			'rollno': self.rollno	
		})

class SchoolProfile(models.Model):
	school = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=40)
	email = models.EmailField(max_length=50)
	phone = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.school.username