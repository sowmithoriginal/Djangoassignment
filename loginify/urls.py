from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test_view'),  # Test view
    path('login/', views.login_view, name='login_view'),  # Login page
    path('signup/', views.signup_view, name='signup_view'), # Signup URL
    path('users/', views.get_all_users, name='get_all_users'),
    path('user/<str:email>/', views.get_user_by_email, name='get_user_by_email'),
    path('user/update/<str:email>/', views.update_user, name='update_user'),
    path('user/delete/<str:email>/', views.delete_user, name='delete_user'),
]