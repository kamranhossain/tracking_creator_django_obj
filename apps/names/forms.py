from django import forms
from apps.names.models import Name

class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ('english_representation', 'vernacular_representation')