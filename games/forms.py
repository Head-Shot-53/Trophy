from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        widgets = {
            'platform':forms.CheckboxSelectMultiple(),
        }