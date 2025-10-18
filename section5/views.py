from django.shortcuts import render
from django.http import HttpResponse

def section5_view(request):
    return render(request, 'section5.html')

