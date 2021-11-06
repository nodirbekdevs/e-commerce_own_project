from django.urls import path
from ..view import product_views as views

urlpatterns = [
    path('', views.get_products, name='get_products'),
    path('<str:pk>/', views.get_product, name='get_product'),
    path('top/', views.get_top_products, name='get_top_products'),
    path('<str:pk>/review/', views.create_product_review, name='create_product_review'),
    path('upload/', views.upload_image, name='upload_image'),
    path('create/', views.create_product, name='create_product'),
    path('update/<str:pk>/', views.update_product, name='update_product'),
    path('delete/<str:pk>/', views.delete_product, name='delete_product'),
]