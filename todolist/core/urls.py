from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.RegistrationView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('user', views.UserView.as_view(), name='user'),
    path('update_password', views.UpdatePasswordView.as_view(), name='update_password'),
]
