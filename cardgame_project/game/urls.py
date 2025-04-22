from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dragon-tiger/', views.play_dragon_tiger, name='play_dragon_tiger'),
    path('', views.dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
