from django.shortcuts import render
from .forms import СoefficientForm


def mat_vvoda(request):
    form = СoefficientForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = (form.cleaned_data)
        print (data["address"])

        new_form = form.save()

    return render(request, 'mat_vvoda/mat_vvoda.html', locals())






