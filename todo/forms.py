from django import forms
from .models import Todo

class TodoModelForm(forms.ModelForm):
    
    class Meta:
        model = Todo   
        fields = (
            'title',
            'description',
            'date_of_execution'
        )

