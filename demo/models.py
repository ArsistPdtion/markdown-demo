from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.

class Dictory(models.Model):
    desc = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    summary = models.FileField(upload_to='md_file/')

    def __str__(self):
        return self.desc

    def get_file_content(self):
        return self.summary

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    content = MDTextField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

class DocumentDemo(models.Model):
    name = models.CharField('file name',max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    content = MDTextField()

    def __str__(self):
        return self.name
