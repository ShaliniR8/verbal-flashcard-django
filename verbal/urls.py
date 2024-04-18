"""verbal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import flash.views as f

urlpatterns = [
    path('', f.welcome, name = 'welcome'),
    path('<int:topic_id>/', f.home_view),
    path('loading/', f.redirect_view, name = 'loading'),
    path('create-topic/', f.create_topic, name='create-topic'),
    path('edit-topic', f.edit_topic, name='edit-topic'),
    path('create-tag/', f.create_tag, name='create-tag'),
    path('remove-tag/', f.remove_tag, name='remove-tag'),
    path('admin/', admin.site.urls),
]
