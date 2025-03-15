from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    author = forms.CharField(max_length=100, required=True)
    publication_year = forms.IntegerField(min_value=1000, max_value=9999, required=True)

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "<script>" in title:  # Basic XSS prevention
            raise forms.ValidationError("Invalid characters in title")
        return title

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "<script>" in title:  # Basic XSS prevention
            raise forms.ValidationError("Invalid characters in title")
        return title