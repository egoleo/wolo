from django.conf.urls.defaults import *

urlpatterns = patterns('wolo.contacts.views.views',
	(r'^$', 'list'),
    (r'^person/add/$','person.add'),
)
