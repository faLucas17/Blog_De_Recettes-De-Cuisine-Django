from django import forms
from .models import Article #importons le modele article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article # le model auquel il est lié
        fields = ['titre', 'resume', 'contenu', 'image'] #les champs à inclure dans le formulaire
        widgets = {
            'titre': forms.TextInput(attrs={'class':'form-control'}),
            'resume': forms.TextInput(attrs={'class':'form-control'}),
            'contenu': forms.Textarea(attrs={'class':'form-control', 'style': 'height: 100px; resize: none;'}),
        }