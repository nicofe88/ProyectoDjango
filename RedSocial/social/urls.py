from django.urls import path
from .views import signup

urlpatterns = [
    path('social/signup/', signup, name='signup')
]