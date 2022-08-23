from django.urls import path, include
from .views import *
from . import views

app_name = "main"
urlpatterns = [
    path('', views.movie_list_create),
    path('review/', views.review_created),
    path('<int:movie_pk>/', views.movie_detail_update_delete),
    path('review/<int:review_pk>/', views.review_detail_update_delete),
    path("accounts/", include('accounts.urls')),
]