"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display',views.display),
    path('display1/<a>',views.display1),
    path('display2/<int:c>',views.display2),
    path('reversename/<b>',views.reversename),
    path('abc',views.abc),
    path('form',views.form),
    path('fars',views.fars),
    path('fact',views.fact),
    path('naame',views.naame),
    path('register',views.register),
    path('allstudents',views.view_students),
    path('searching',views.search_student),
    path('deleting',views.delete_student),
    path('updating',views.update_student),
    path('template1',views.temp1),
    path('template2',views.temp2)
]
