from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import *
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404

from django.contrib import messages

from courses.models import *

def home(request,template="courses/home.html",page_template="courses/course_page.html"):
    context = {
        "courses": Course.objects.all().order_by("title"),
        "page_template": page_template
    }
    if request.is_ajax():
        template = page_template
    return render_to_response(template,context,context_instance=RequestContext(request))

def filter_by_category(request,slug,template="courses/home.html",page_template="courses/course_page.html"):
    category = Category.objects.get(slug=slug)
    context = {
        "courses": Course.objects.filter(categories__in=[category.id]).order_by("title"),
        "page_template": page_template,
        "active_category":category,
        "page_title":category.name
    }
    if request.is_ajax():
        template = page_template
    return render_to_response(template,context,context_instance=RequestContext(request))

def filter_by_school(request,slug,template="courses/home.html",page_template="courses/course_page.html"):
    school = School.objects.get(slug=slug)
    context = {
        "courses": Course.objects.filter(school=school).order_by("title"),
        "page_template": page_template,
        "page_title":school.name
    }
    if request.is_ajax():
        template = page_template
    return render_to_response(template,context,context_instance=RequestContext(request))


def filter_by_materials(request,slug,template="courses/home.html",page_template="courses/course_page.html"):
    material = Material.objects.get(slug=slug)
    context = {
        "courses": Course.objects.filter(materials__in=[material.id]).order_by("title"),
        "page_template": page_template,
        "page_title":material.name
    }
    if request.is_ajax():
        template = page_template
    return render_to_response(template,context,context_instance=RequestContext(request))

import json
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Exact, Clean
def ajax_search(request):
    query = SearchQuerySet().filter(content=AutoQuery(request.POST.get("query","")))
    result = [{"name":str(a.object),"url":a.object.get_absolute_url()} for a in query]
    return HttpResponse(json.dumps(result), mimetype="application/json")
