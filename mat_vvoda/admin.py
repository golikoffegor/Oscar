from django.contrib import admin
from .models import *

class СoefficientAdmin(admin.ModelAdmin):
	list_display = ["address", "name_author"]
	list_filter = ["name_author"]
	search_fields = ["address"]

	class Meta:
		model = Сoefficient



admin.site.register(Сoefficient, СoefficientAdmin)

