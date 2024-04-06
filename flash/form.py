from django import forms
from .models import Topic, Tag

class CardForm(forms.ModelForm):
     class Meta:
          model = Topic
          fields = ['topic', 'description']

class TagForm(forms.ModelForm):
     class Meta:
          model = Tag
          fields = ['tag']
