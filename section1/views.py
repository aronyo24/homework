from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def section1_view(request):
    return render(request, 'section1.html')
