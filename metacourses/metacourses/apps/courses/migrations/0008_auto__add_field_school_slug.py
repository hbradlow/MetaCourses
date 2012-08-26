# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.slug'
        db.add_column('courses_school', 'slug',
                      self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, default='', unique=True, populate_from='name', overwrite=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.slug'
        db.delete_column('courses_school', 'slug')


    models = {
        'courses.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        },
        'courses.course': {
            'Meta': {'object_name': 'Course'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['courses.Category']", 'symmetrical': 'False'}),
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'null': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['courses.School']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'courses.school': {
            'Meta': {'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        }
    }

    complete_apps = ['courses']