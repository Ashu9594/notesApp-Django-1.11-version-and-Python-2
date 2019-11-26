from django import forms
from notesApp.models import notes


class NotesForm(forms.ModelForm):  
    class Meta:  
        model = notes  
        fields = "__all__"  