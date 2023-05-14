from django import forms

class WordInput(forms.Form):
    word = forms.CharField(label='Слово', max_length=100)
     