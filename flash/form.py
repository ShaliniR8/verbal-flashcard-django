from django import forms
from .models import Topic, Tag, UseCase, Comparison, ComparisonRow

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

class ComparisonForm(forms.ModelForm):
    class Meta:
        model = Comparison
        fields = ['comparison1', 'comparison2']

class ComparisonRowForm(forms.ModelForm):
    class Meta:
        model = ComparisonRow
        fields = ['row1', 'row2']