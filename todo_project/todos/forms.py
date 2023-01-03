from .models import Todo
from django import forms
from django.forms import ModelForm

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['description', 'completed']
        widgets = {
            'completed': forms.CheckboxInput()
        }