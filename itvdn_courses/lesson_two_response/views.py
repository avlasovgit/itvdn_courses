from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
# Create your views here.

def hello_response(request):
	return HttpResponse('Hello in response!')

def http_redirect(request):
	#return redirect('/lesson_two/item/1989/22/')
	#return redirect('hello_response')
	return redirect('blog_articles')

def fun1(request):
	return HttpResponse('Hello in redirect!')

def render_html(request):
	_html = '''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>TEST</title>
</head>
<body>
	<h1>Тестовый рендер html</h1>
	<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus, odit sint, officiis, voluptatem cum debitis ipsam rem doloribus dignissimos velit atque magni enim. Eaque odit sapiente eos culpa quidem provident.</p>
</body>
</html>'''
	return HttpResponse(_html)

def render_template(request):
	return render(request, 'main.html', {})

def render_response(request):
	return render_to_response('main_render.html', {})

def form_hendler(request):
	if request.POST:
		return HttpResponse('Request is POST')
	else:
		return HttpResponse('Request is GET')
