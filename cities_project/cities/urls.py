from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('cities/', views.CityList.as_view(), name='city-list'),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name='city-detail'),
    path('attractions/', views.AttractionList.as_view(), name='attraction-list'),
    path('attractions/<int:pk>/', views.AttractionDetail.as_view(), name='attraction-detail'),
    path('reviews/', views.ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]
