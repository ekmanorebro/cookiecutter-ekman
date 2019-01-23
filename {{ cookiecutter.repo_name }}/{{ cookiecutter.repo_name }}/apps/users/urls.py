from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
  path('register/', views.RegisterFormView.as_view(), name="register"),
  path('login/', views.UserLoginView.as_view(), name="login"),
  path('logout/', views.UserLogoutView.as_view(), name="logout"),
  path('<str:username>/', views.UserDetailView.as_view(), name="detail"),
]