# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Dataset'
        # db.create_table(u'news_dataset', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('docid', self.gf('django.db.models.fields.IntegerField')()),
        #     ('headline', self.gf('django.db.models.fields.TextField')()),
        #     ('trailText', self.gf('django.db.models.fields.TextField')()),
        #     ('byline', self.gf('django.db.models.fields.TextField')()),
        #     ('body', self.gf('django.db.models.fields.TextField')()),
        #     ('webURL', self.gf('django.db.models.fields.TextField')()),
        #     ('published', self.gf('django.db.models.fields.DateTimeField')()),
        #     ('imageLink', self.gf('django.db.models.fields.TextField')()),
        #     ('tags', self.gf('django.db.models.fields.TextField')()),
        #     ('section', self.gf('django.db.models.fields.TextField')()),
        #     ('clicks', self.gf('django.db.models.fields.IntegerField')()),
        #     ('upvotes', self.gf('django.db.models.fields.IntegerField')()),
        #     ('downvotes', self.gf('django.db.models.fields.IntegerField')()),
        # ))
        # db.send_create_signal(u'news', ['Dataset'])

        # # Adding model 'Hot'
        # db.create_table(u'news_hot', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('docid', self.gf('django.db.models.fields.IntegerField')()),
        #     ('published', self.gf('django.db.models.fields.DateTimeField')()),
        #     ('hottness', self.gf('django.db.models.fields.FloatField')()),
        # ))
        # db.send_create_signal(u'news', ['Hot'])

        # # Adding model 'Info'
        # db.create_table(u'news_info', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('doc_id', self.gf('django.db.models.fields.IntegerField')()),
        #     ('user_id', self.gf('django.db.models.fields.IntegerField')()),
        #     ('user_like', self.gf('django.db.models.fields.IntegerField')()),
        # ))
        # db.send_create_signal(u'news', ['Info'])

        # Adding model 'Categories'
        db.create_table(u'news_categories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('occurences', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'news', ['Categories'])


    def backwards(self, orm):
        # Deleting model 'Dataset'
        db.delete_table(u'news_dataset')

        # Deleting model 'Hot'
        db.delete_table(u'news_hot')

        # Deleting model 'Info'
        db.delete_table(u'news_info')

        # Deleting model 'Categories'
        db.delete_table(u'news_categories')


    models = {
        u'news.categories': {
            'Meta': {'object_name': 'Categories'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occurences': ('django.db.models.fields.IntegerField', [], {})
        },
        u'news.dataset': {
            'Meta': {'object_name': 'Dataset'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'byline': ('django.db.models.fields.TextField', [], {}),
            'clicks': ('django.db.models.fields.IntegerField', [], {}),
            'docid': ('django.db.models.fields.IntegerField', [], {}),
            'downvotes': ('django.db.models.fields.IntegerField', [], {}),
            'headline': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageLink': ('django.db.models.fields.TextField', [], {}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'section': ('django.db.models.fields.TextField', [], {}),
            'tags': ('django.db.models.fields.TextField', [], {}),
            'trailText': ('django.db.models.fields.TextField', [], {}),
            'upvotes': ('django.db.models.fields.IntegerField', [], {}),
            'webURL': ('django.db.models.fields.TextField', [], {})
        },
        u'news.hot': {
            'Meta': {'object_name': 'Hot'},
            'docid': ('django.db.models.fields.IntegerField', [], {}),
            'hottness': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'news.info': {
            'Meta': {'object_name': 'Info'},
            'doc_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'user_like': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['news']