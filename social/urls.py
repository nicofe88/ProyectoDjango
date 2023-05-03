from django.urls import path
from .views import signup
from . import views

urlpatterns = [

    path('', views.social_index, name='social_index'),
    path('signup/', views.signup, name='signup'),
   
   
    
]