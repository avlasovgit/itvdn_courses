from django.conf.urls import url
from . import views
from django.urls import include

extra_patterns = [
	url(r'^report/$', views.report), #http://localhost:5000/lesson_two_part2/extra/report/
	url(r'^report/(?P<id>[0-9]+)/$', views.report), #http://localhost:5000/lesson_two_part2/extra/report/5454/
	url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\d]+)/history/$', views.history, name = 'history'), #http://localhost:5000/lesson_two_part2/extra/dfgd-454/history/
	url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\d]+)/edit/$', views.edit, name = 'edit'), #http://localhost:5000/lesson_two_part2/extra/dfgd-454/edit/
	url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\d]+)/discuss/$', views.discuss, name = 'discuss'), #http://localhost:5000/lesson_two_part2/extra/dfgd-454/discuss/
	url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\d]+)/permissions/$', views.permissions, name = 'permissions'), #http://localhost:5000/lesson_two_part2/extra/dfgd-454/permissions/
	url(r'^variant/', include([
		url(r'^(?P<page_slug>[\w]+)-(?P<page_id>[\d]+)/', include([
			url(r'^history/$', views.history, name = 'variant_history'), #http://localhost:5000/lesson_two_part2/extra/variant/dfgd-4754/history/
			url(r'^edit/$', views.edit, name = 'variant_edit'), #http://localhost:5000/lesson_two_part2/extra/variant/dfgd-4754/edit/
			url(r'^discuss/$', views.discuss, name = 'variant_discuss'), #http://localhost:5000/lesson_two_part2/extra/variant/dfgd-4754/discuss/
			url(r'^permissions/$', views.permissions, name = 'variant_permissions') #http://localhost:5000/lesson_two_part2/extra/variant/dfgd-4754/permissions/
		]))
	]))
]

urlpatterns = [
	url(r'^blog/(page-(\d+)/)?$', views.blog_articles, name = 'blog_articles'), #http://localhost:5000/lesson_two_part2/blog/page-2/
	url(r'^comment/(?:page-(?P<page_number>\d+)/)?$', views.comment, name = 'comment'), #http://localhost:5000/lesson_two_part2/comment/page-2/
	url(r'^blog/(?P<year>[0-9]{4})/$', views.optional_args, {'foo': 'bar'}, name = 'optional_args',), #http://localhost:5000/lesson_two_part2/blog/2255/
	url(r'^extra/', include(extra_patterns)),	 
]
