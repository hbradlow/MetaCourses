from django.db import models
from django.contrib import admin
from django_extensions.db.fields import AutoSlugField
from django.db.models import permalink

class School(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="name",unique=True)
    def __unicode__(self):
        return self.name
    @permalink
    def get_absolute_url(self):
        return ("filter_by_school",[self.slug])
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="name",unique=True)
    def __unicode__(self):
        return self.name
    @permalink
    def get_absolute_url(self):
        return ("filter_by_category",[self.slug])
class Material(models.Model):
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="name",unique=True)
    def __unicode__(self):
        return self.name
    @permalink
    def get_absolute_url(self):
        return ("filter_by_materials",[self.slug])
class Course(models.Model):
    types = [
            ("edx","edX"),
            ("coursera","Coursera"),
            ("mit","MIT Open Courseware"),
    ]
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=500)
    type = models.CharField(max_length=100,choices=types)
    course_id = models.CharField(max_length=50)
    school = models.ForeignKey(School,null=True)
    categories = models.ManyToManyField(Category)
    materials = models.ManyToManyField(Material)
    image_url = models.URLField(max_length=500,null=True)

    def __unicode__(self):
        return self.type + ": " + self.title
    def get_absolute_url(self):
        return self.link
admin.site.register(Course)
