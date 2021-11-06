from django.urls import path
from ..view import order_views as views

urlpatterns = [
    path('', views.get_orders, name='get_orders'),
    path('add/', views.add_order_items, name='add_order_items'),
    path('myOrders/', views.get_my_orders, name='get_my_orders'),
    path('<str:pk>/', views.get_order_by_id, name='get_order_by_id'),
    path('<str:pk>/pay/', views.update_order_to_paid, name='update_order_to_paid'),
    path('<str:pk>/deliver/', views.update_order_to_delivered, name='update_order_to_delivered'),
]