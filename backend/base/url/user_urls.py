from django.urls import path
from ..view import user_views as views

urlpatterns = [
    path('', views.get_users, name='users'),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('<str:pk>/', views.get_user_by_id, name='get_user_by_id'),
    path('profile/', views.get_user_profile, name='user_profile'),
    path('profile/update/', views.update_user_profile, name='user_profile_update'),
    path('update/<str:pk>/', views.update_user, name='update_user'),
    path('delete/<str:pk>/', views.delete_user, name='delete_user'),
]
