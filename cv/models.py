from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class Category(models.Model):
    label = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    cover = models.ImageField(upload_to="articles")

    class Meta :
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.label

    def display(self):
        return self.label

class Experience(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    address = models.TextField(null=True, blank=True, max_length=100)
    short_desc = models.TextField(max_length=100)
    content = models.TextField(max_length=3000)
    start_the = models.DateField(null=True, blank=True, auto_now_add=False, verbose_name="Date de debut")
    end_the = models.DateField(null=True, blank=True, auto_now=False, verbose_name="Date de fin")
    cover = models.ImageField(upload_to="articles")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    def display(self):
        return self.title

    def __unicode__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    mail = models.EmailField(max_length=50)
    phone = PhoneNumberField(max_length=20)

    def display(self):
        return self.name

    def __unicode__(self):
        return self.name
