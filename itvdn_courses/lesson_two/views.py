from django.http import HttpResponse

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

def show_url_param(request, word):
	return HttpResponse('Welcome to {}'.format(word))

def page(request, num = '1'):
	if num == '1':
		return HttpResponse('Welcome to first book page!')
	else:
		return HttpResponse('Welcome to My book page number - {}'.format(num)) 
