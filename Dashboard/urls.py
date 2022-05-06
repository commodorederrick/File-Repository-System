from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Dashboard-home'),
    path('signup/', views.signup, name='Dashboard-signup'),
    path('login/', views.login, name='Dashboard-login'),
    path('Dashboard/', views.index, name='Dashboard-index'),
    path('pdf/', views.pdf, name='Dashboard-pdf'),
    path('upload/', views.uploadfunc, name='Dashboard-upload'),
    path('journal/', views.Journalfunc, name='Dashboard-journals'),
]
