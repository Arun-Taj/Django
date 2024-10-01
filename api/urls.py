from django.urls import path
from .views import get_users, create_users, update_user

urlpatterns = [
    path('user/', get_users, name='get_users'),
    path('user/create', create_users, name='create_users'),
    path('user/<int:pk>', update_user, name='update_user'),

]
  