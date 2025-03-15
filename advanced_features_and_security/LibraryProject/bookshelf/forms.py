from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "<script>" in title:  # Basic XSS prevention
            raise forms.ValidationError("Invalid characters in title")
        return title