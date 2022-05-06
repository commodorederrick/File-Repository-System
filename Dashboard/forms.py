from django import forms
from . models import person, upload
from . models import Book


class personForm(forms.ModelForm):
    class Meta:
        model = person
        fields = [
            'first_name',
            'last_name',
            'email',
            'member_ID',
            'pin',
            'Confirm_pin']


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = '__all__'

class uploadForm(forms.ModelForm):
    class Meta:
        model = upload
        fields = ['title', 'author', 'pdf']
