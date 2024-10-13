from django import forms

class SearchForm(forms.Form):
    query = forms.CharField( label='search' , max_length=100 )