from django import forms
from .models import Topic, Tag

class CardForm(forms.ModelForm):
     class Meta:
          model = Topic
          fields = ['word', 'meaning', 'example1', 'example2', 'example3']

class TagForm(forms.ModelForm):
     class Meta:
          model = Tag
          fields = ['tag']
