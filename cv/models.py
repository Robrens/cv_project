from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

choices = []
for i in range(1, 5):
    choices.append((i,i))

level = [
    ('novice', 'novice'),
    ('advanced-beginer', 'advanced-beginer'),
    ('competent', 'competent'),
    ('professionnel', 'professionnel'),
    ('expert', 'expert'),
]


class Category(models.Model):
    label = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    cover = models.ImageField(upload_to="articles")

    class Meta :
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.label


class Education(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    address = models.TextField(max_length=100)
    short_desc = models.TextField(null=True, blank=True, max_length=100)
    content = models.TextField(null=True, blank=True, max_length=3000)
    start_the = models.DateField(null=True, blank=True, auto_now_add=False, verbose_name="Date de debut")
    end_the = models.DateField(null=True, blank=True, auto_now=False, verbose_name="Date de fin")
    cover = models.ImageField(null=True, blank=True, upload_to="articles")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    def __unicode__(self):
        return self.slug


class Experience(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    address = models.TextField(null=True, blank=True, max_length=100)
    short_desc = models.TextField(null=True, blank=True, max_length=100)
    content = models.TextField(null=True, blank=True, max_length=3000)
    start_the = models.DateField(
        null=True, blank=True, auto_now_add=False, verbose_name="Date de debut")
    end_the = models.DateField(
        null=True, blank=True, auto_now=False, verbose_name="Date de fin")
    cover = models.ImageField(null=True, blank=True, upload_to="articles")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False)

    def __unicode__(self):
        return self.slug


class SpareTime(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    short_desc = models.TextField(null=True, blank=True, max_length=100)
    cover = models.ImageField(null=True, blank=True, upload_to="articles")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    def __unicode__(self):
            return self.slug


class Abilitie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    lvl = models.CharField(choices=level, default='novice', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    def __unicode__(self):
            return self.slug


class User(models.Model):
    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    phone = PhoneNumberField(max_length=20)

    def __unicode__(self):
        return self.name
