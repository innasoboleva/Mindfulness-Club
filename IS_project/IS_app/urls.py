from django.urls import path
from . import views

urlpatterns = [
    path('api/hello_world/', views.index, name='hello_world'),
    path('api/create_new_user', views.create_user, name='create_user')
]