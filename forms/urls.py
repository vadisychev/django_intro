from django.urls import path

from . import views


urlpatterns = [
    path('registration_book/', views.registration_book, name='registration_book'),
    path('input_info/', views.input_info, name='input_info'),
]
