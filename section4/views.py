from django.shortcuts import render
from django.http import HttpResponse

# Robust view for section3. Keeps import-time simple to avoid AttributeError
def section4_view(request):
    return render(request, 'section3.html')

