"""banking_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from banking_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('new_client/', new_client, name='new_client'),
    path('create_client', create_client, name='create_client'),
    path('new_account/', new_account, name='new_account'),
    path('create_account', create_account, name='create_account'),
    path('new_statement/', new_statement, name='new_statement'),
    path('create_statement', create_statement, name='create_statement'),
]
