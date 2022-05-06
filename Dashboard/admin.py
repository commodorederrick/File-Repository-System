from django.contrib import admin

from Dashboard.models import upload
from .models import Book, person

# Register your models here.
admin.site.register(person)
admin.site.register(upload)
