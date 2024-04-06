from django.contrib import admin
from .models import Topic, UseCase, Comparison, ComparisonRow, Tag, Note
# Register your models here.
admin.site.register( Topic )
admin.site.register( UseCase )
admin.site.register( Comparison )
admin.site.register( ComparisonRow )
admin.site.register( Tag )
admin.site.register( Note )