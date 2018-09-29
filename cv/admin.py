# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Experience, User
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('label',)
    prepopulated_fields = {'slug': ('label',)}

admin.site.register(Category, CategoryAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_the', 'end_the', 'short_desc', 'category')
    search_fields = ('title', 'start_the')
    list_filter = ('category',)
    fieldsets = (
        ("Général", {
            'fields': (('title', 'slug'),
                       ('category', 'start_the', 'end_the',),),
        }),
        ("Contenu", {
            'fields': (('cover', 'short_desc',),
                       'content','address'),
        })
    )
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Experience, ExperienceAdmin)


class userAdmin(admin.ModelAdmin):
    list_display = ('name', 'firstName', 'address', 'mail', 'phone')
    fieldsets = (
        ("Général", {
            'fields': (('name', 'firstName'),
                       ('address',),),
        }),
        ("Contenu", {
            'fields': (('mail',),
                       'phone',),
        })
    )


admin.site.register(User, userAdmin)
