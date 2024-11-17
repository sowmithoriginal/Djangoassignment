from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test_view'),  # Test view
    path('login/', views.login_view, name='login_view'),  # Login page
    path('signup/', views.signup_view, name='signup_view'), # Signup URL
]