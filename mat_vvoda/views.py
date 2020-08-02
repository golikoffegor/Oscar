from django.shortcuts import render
from .forms import CoefficientForm

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import *
from .serializers import CoefficientSerializer, ResultsSerializer

from .oscar_python.Construction import Constructions
from .oscar_python.Mat_trubs import Mat_trubs

class CoefficientView(APIView):
    def get(self, request):
        #На выходе присылает лист (список) из словарей
        coefficients = Coefficient.objects.all()
        serializer = CoefficientSerializer(coefficients, many = True)
        return Response({"coefficients": serializer.data})

    def post(self, request):
        #Запрос на публикацию надо отправлять словарем
        coefficients = request.data.get("coefficients")
        serializer = CoefficientSerializer(data = coefficients)
        if serializer.is_valid(raise_exception = True):
            coefficient_saved = serializer.save()
            for key, value in serializer.data.items():
                if key == "address":
                    name_address = value
                    CO2_1 = Mat_trubs(serializer)
                    CO2_2 = Constructions(serializer)
                    all_results = Results(address = name_address, result_CO2_1 = CO2_1.trubs(), result_CO2_2 = CO2_2.construction())
                    all_results.save()
                    
                    #return Response(serializer.data)

        #return Response(serializer.data)

            #CO = Mat_trubs(serializer)
        #return Response(CO.trubs())

        return Response({"success": "Coefficients '{}' created successfully".format(coefficient_saved)})

    def put(self, request, pk):
        saved_coefficient = get_object_or_404(Coefficient.objects.all(), pk = pk)
        data = request.data.get('coefficients')
        serializer = CoefficientSerializer(instance = saved_coefficient, data = data, partial = True)
        if serializer.is_valid(raise_exception = True):
            coefficient_saved = serializer.save()
        return Response({"success": "Coefficients '{}' updated successfully".format(coefficient_saved)})

    def delete(self, request, pk):
        coefficients = get_object_or_404(Coefficient.objects.all(), pk = pk)
        coefficients.delete()
        return Response({"message": "Coefficients with id `{}` has been deleted.".format(pk)}, status = 200)

class ResultsView(APIView):
    def get(self, request):
        #На выходе присылает лист (список) из словарей
        results = Results.objects.all()
        serializer = ResultsSerializer(results, many = True)
        return Response({"results": serializer.data})

    def post(self, request):
        #Запрос на публикацию надо отправлять словарем
        results = request.data.get("results")
        serializer = ResultsSerializer(data = results)
        if serializer.is_valid(raise_exception = True):
            results_saved = serializer.save()
        return Response({"success": "Results '{}' created successfully".format(results_saved)})

    def put(self, request, pk):
        saved_results = get_object_or_404(Results.objects.all(), pk = pk)
        data = request.data.get('results')
        serializer = ResultsSerializer(instance = saved_results, data = data, partial = True)
        if serializer.is_valid(raise_exception = True):
            results_saved = serializer.save()
        return Response({"success": "Results '{}' updated successfully".format(results_saved)})

    def delete(self, request, pk):
        results = get_object_or_404(Results.objects.all(), pk = pk)
        results.delete()
        return Response({"message": "Results with id `{}` has been deleted.".format(pk)}, status = 200)


def mat_vvoda(request):
    form = CoefficientForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = (form.cleaned_data)
        print (data["address"])

        new_form = form.save()

    return render(request, 'mat_vvoda/mat_vvoda.html', locals())







