from django.urls import path

from . import views


urlpatterns = [
    path('result/', views.index, name='index_test'),
    path('input_info/', views.input_info, name='input_info'),
]
