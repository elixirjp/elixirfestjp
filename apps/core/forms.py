from django import forms

from core.models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('user', 'email', 'title', 'description', 'comment')
