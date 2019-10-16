from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^items$', views.items, name = 'items'), #http://localhost:5000/lesson_two/items
    url(r'^item/2003/$', views.special_case_2003, name = 'special_case_2003'), #http://localhost:5000/lesson_two/item/2003/
    url(r'^item/([0-9]{4,5})/$', views.year_archive, name = 'year_archive'), #http://localhost:5000/lesson_two/item/1989/
    url(r'^item/([0-9]{4})/([0-9]{2})/$', views.month_arhive, name = 'month_arhive'), #http://localhost:5000/lesson_two/item/1989/22/
    url(r'^item/(?P<year>[\d]{4})/(?P<month>[\d]{2})/(?P<day>[\d]{2})/$', views.day_arhive, name = 'day_arhive'), #http://localhost:5000/lesson_two/item/1989/22/22
    url(r'^item/(?P<year>[\d]{4})/(?P<month>[\d]{2})/(?P<day>[\d]{2})/test/$', views.day_arhive, name = 'day_arhive_test'), #http://localhost:5000/lesson_two/item/2000/23/12/test/
		url(r'^item/(?P<word>[\w]+)/$', views.show_url_param, name = 'show_url_param'), #http://localhost:5000/lesson_two/item/ejgsdfgjkljskljdgklfjksdg/
		url(r'^book/$', views.page, name = 'page'), #http://localhost:5000/lesson_two/book/page4165/
		url(r'^book/page(?P<num>[0-9]+)/$', views.page, name = 'page'), #http://localhost:5000/lesson_two/book/page4165/
    url(r'^$', views.home, name = 'home'),#http://localhost:5000/lesson_two
]
