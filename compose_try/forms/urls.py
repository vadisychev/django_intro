from django.urls import path

from . import views


urlpatterns = [
    path('registration_book/', views.registration_book, name='registration_book'),
    path('input_info/', views.input_info, name='input_info'),
    path('input_info_bootstrap/', views.input_info_bootstrap, name='input_info_bootstrap'),
    path('registration_book_bootstrap/', views.registration_book_bootstrap, name='registration_book_bootstrap')
]
