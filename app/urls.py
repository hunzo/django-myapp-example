from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('upload', views.upload_file, name="upload_file"),
    path('add/', views.add_email, name="add_email"),
    path('add-mail-to-group/', views.add_email_to_group, name="add_email_to_group")
]