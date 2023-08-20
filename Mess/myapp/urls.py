from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='Home'),
    path("feedback",views.feedback,name='feedback'),
    path("feedback_success",views.feedback_success,name='feedback_success'),
    path("suggest",views.suggest,name='suggest'),
    path("report",views.report,name='report'),
    path('menu', views.menuweb, name='menuweb'),
]