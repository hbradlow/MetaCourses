# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table('courses_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('courses', ['School'])

        # Adding field 'Course.school'
        db.add_column('courses_course', 'school',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.School'], null=True),
                      keep_default=False)

        # Adding field 'Course.category'
        db.add_column('courses_course', 'category',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table('courses_school')

        # Deleting field 'Course.school'
        db.delete_column('courses_course', 'school_id')

        # Deleting field 'Course.category'
        db.delete_column('courses_course', 'category')


    models = {
        'courses.course': {
            'Meta': {'object_name': 'Course'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['courses.School']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'courses.school': {
            'Meta': {'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['courses']