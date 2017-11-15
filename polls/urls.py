from django.conf.urls import url

from . import views

urlpatterns = [
	# /polls/
	url(r'^$', views.index, name="index"),

	# polls/5
	url(r'^$')
]
