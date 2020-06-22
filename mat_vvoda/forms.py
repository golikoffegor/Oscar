from django import forms
from .models import *

class СoefficientForm(forms.ModelForm):

	class Meta:
		model = Сoefficient
		exclude = [""]