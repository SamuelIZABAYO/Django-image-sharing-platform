from django.urls import path

from . import views

urlpatterns = [
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='image_detail'),
    path('create/', views.image_create, name='create'),
]
