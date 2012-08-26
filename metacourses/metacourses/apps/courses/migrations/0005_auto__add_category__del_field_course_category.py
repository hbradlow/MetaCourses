# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('courses_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('courses', ['Category'])

        # Deleting field 'Course.category'
        db.delete_column('courses_course', 'category')

        # Adding M2M table for field categories on 'Course'
        db.create_table('courses_course_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm['courses.course'], null=False)),
            ('category', models.ForeignKey(orm['courses.category'], null=False))
        ))
        db.create_unique('courses_course_categories', ['course_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('courses_category')

        # Adding field 'Course.category'
        db.add_column('courses_course', 'category',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True),
                      keep_default=False)

        # Removing M2M table for field categories on 'Course'
        db.delete_table('courses_course_categories')


    models = {
        'courses.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'courses.course': {
            'Meta': {'object_name': 'Course'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['courses.Category']", 'symmetrical': 'False'}),
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