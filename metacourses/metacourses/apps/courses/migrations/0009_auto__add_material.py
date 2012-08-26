# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Material'
        db.create_table('courses_material', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, unique=True, populate_from='name', overwrite=False)),
        ))
        db.send_create_signal('courses', ['Material'])

        # Adding M2M table for field materials on 'Course'
        db.create_table('courses_course_materials', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm['courses.course'], null=False)),
            ('material', models.ForeignKey(orm['courses.material'], null=False))
        ))
        db.create_unique('courses_course_materials', ['course_id', 'material_id'])


    def backwards(self, orm):
        # Deleting model 'Material'
        db.delete_table('courses_material')

        # Removing M2M table for field materials on 'Course'
        db.delete_table('courses_course_materials')


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
            'materials': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['courses.Material']", 'symmetrical': 'False'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['courses.School']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'courses.material': {
            'Meta': {'object_name': 'Material'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        },
        'courses.school': {
            'Meta': {'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        }
    }

    complete_apps = ['courses']