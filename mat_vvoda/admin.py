from django.contrib import admin
from .models import *

class CoefficientAdmin(admin.ModelAdmin):
    list_display = ["address", "author", "id"]
    list_filter = ["author"]
    search_fields = ["address"]

    class Meta:
        model = Coefficient

class ResultsAdmin(admin.ModelAdmin):
    list_display = ["address", "id"]
    search_fields = ["address"]

    class Meta:
        model = Coefficient



admin.site.register(Coefficient, CoefficientAdmin)
admin.site.register(Author)
admin.site.register(Results, ResultsAdmin)

