from django import forms
from .models import Topic, Tag, UseCase

class TopicForm(forms.ModelForm):
     class Meta:
          model = Topic
          fields = ['topic', 'description']

class TagForm(forms.ModelForm):
     class Meta:
          model = Tag
          fields = ['tag']

class UseCaseForm(forms.ModelForm):
    class Meta:
        model = UseCase
        fields = ['description']