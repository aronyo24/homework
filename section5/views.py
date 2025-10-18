from django.shortcuts import render
from django.http import HttpResponse

# Robust view for section4. Keeps import-time simple to avoid AttributeError
def section5_view(request):
    return render(request, 'section3.html')

