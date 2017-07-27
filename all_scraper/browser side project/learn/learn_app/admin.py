# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Person
from django.contrib import admin

# Register your models here.
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('title','pub_date','update_time',)

admin.site.register(Person)
# admin.site.register(Person, ArticleAdmin)