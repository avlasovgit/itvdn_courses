#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Main page!')

def items(request):
    return HttpResponse('Welcome to http://localhost:5000/lesson_two/items')

def special_case_2003(request):
    return HttpResponse('Welcome to http://localhost:5000/lesson_two/item/2003' )

def year_archive(request, year):
    return HttpResponse('Welcome to year {}'.format(year))

def month_arhive(request, year, month):
    return HttpResponse('Welcome to year - {} month - {}'.format(year, month))

def day_arhive(request, year, month, day):
    return HttpResponse('Welcome to year - {} month - {} day - {}'.format(year, month, day))
