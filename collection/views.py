from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

# This is basically like a getter function if
# a webapp was itself a class
