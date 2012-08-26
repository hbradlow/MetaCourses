from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.views.generic import ListView, DetailView, CreateView, UpdateView, RedirectView

from courses.models import Category, School, Material

urlpatterns = patterns('courses.views',
    url(r'^$', 'home', name='home'),
    url(r'^categories/(?P<slug>[\w\._-]+)/$', 'filter_by_category', name='filter_by_category'),
    url(r'^schools/(?P<slug>[\w\._-]+)/$', 'filter_by_school', name='filter_by_school'),
    url(r'^materials/(?P<slug>[\w\._-]+)/$', 'filter_by_materials', name='filter_by_materials'),

    url(r'^categories/$', ListView.as_view(model=Category), name='categories'),
    url(r'^schools/$', ListView.as_view(model=School), name='schools'),
    url(r'^materials/$', ListView.as_view(model=Material), name='materials'),
    url(r'^ajax_search/$', "ajax_search", name='ajax_search'),
)
