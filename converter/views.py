from django.shortcuts import render
from django.http import HttpResponse
from num2words import num2words

# Create your views here.

def home(request):
    return render(request, 'converter/home.html')

def about(request):
    return render(request, 'converter/about.html')

def convert(request):

    word = ''

    inputnum = request.GET.get('num')
    word = num2words(inputnum).capitalize()
  

    return render(request, 'converter/convert.html', {'word':word})
