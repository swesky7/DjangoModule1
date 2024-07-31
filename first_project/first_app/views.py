from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    my_dict = {'insert_me': "Iam coming from first_app/index.html"}
    return render(request, 'first_app/index.html', context=my_dict)
    # return HttpResponse("Hello, World! This is my first Django project.")


def about(request):
    return HttpResponse("This is the about page.")

# Create your views here.
