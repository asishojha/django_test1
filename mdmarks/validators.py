from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_100_marks(value):
	try:
		value = int(value)
		if not 0 <= value <= 100:
			raise ValidationError(
				_('%(value)s is not a valid option'),
				params={'value': value},
			)
	except ValueError:
		value = str(value).upper()
		if value != 'AB':
			raise ValidationError(
				_('%(value)s is not a valid option'),
				params={'value': value},
			)

def validate_50_marks(value):
	try:
		value = int(value)
		if not 0 <= value <= 50:
			raise ValidationError(
				_('%(value)s is not a valid option'),
				params={'value': value},
			)
	except ValueError:
		value = str(value).upper()
		if value != 'AB':
			raise ValidationError(
				_('%(value)s is not a valid option'),
				params={'value': value},
			)