from django.db import models

# Create your models here.


class person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    member_ID = models.IntegerField()
    pin = models.IntegerField()
    Confirm_pin = models.IntegerField()

    def __str__(self):
        return self.first_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.title


class upload(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.title


class journals(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')

    def __str__(self):
        return self.title
