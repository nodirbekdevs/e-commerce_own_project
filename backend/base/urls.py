from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('users/', include('base.url.user_urls')),
    path('products/', include('base.url.product_urls')),
    path('orders/', include('base.url.order_urls')),
]
