from django.http import HttpResponse
# Create your views here.

def blog_articles(request, a, b): #a = page, b = 2 (число)
	return HttpResponse('blog_articles "{}"  "{}"'.format(a, b))

def comment(request, page_number):
	return HttpResponse('comment {}'.format(page_number))

def optional_args(request, year, foo):
	return HttpResponse('optional_args  {}  {}'.format(year, foo))

def report(request, id = '1'):
	return HttpResponse('report number {}'.format(id))

def history(request, page_slug, page_id):
	return HttpResponse('Welcome to History {} {}'.format(page_slug, page_id))

def edit(request, page_slug, page_id):
	return HttpResponse('Welcome to Edit {} {}'.format(page_slug, page_id))

def discuss(request, page_slug, page_id):
	return HttpResponse('Welcome to Discuss {} {}'.format(page_slug, page_id))

def permissions(request, page_slug, page_id):
	return HttpResponse('Welcome to Permissions {} {}'.format(page_slug, page_id))