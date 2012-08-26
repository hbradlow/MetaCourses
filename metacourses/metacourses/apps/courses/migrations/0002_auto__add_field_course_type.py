# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Course.type'
        db.add_column('courses_course', 'type',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Course.type'
        db.delete_column('courses_course', 'type')


    models = {
        'courses.course': {
            'Meta': {'object_name': 'Course'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['courses']