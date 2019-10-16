from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.hello_response, name = 'hello_response'), #http://localhost:5000/lesson_two_response/
		url(r'^redirect/$', views.http_redirect), #http://localhost:5000/lesson_two_response/redirect/
		url(r'^fun1/$', views.fun1), #http://localhost:5000/lesson_two_response/fun1/
		url(r'^render-html/$', views.render_html), #http://localhost:5000/lesson_two_response/render-html/
		url(r'^render-template/$', views.render_template), #http://localhost:5000/lesson_two_response/render-template/
        url(r'^render-template/form-hendler/$', views.form_hendler, name = 'form_hendler'),
        url(r'^render-response/$', views.render_response), #http://localhost:5000/lesson_two_response/render-response/
]
