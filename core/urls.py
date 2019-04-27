from django.urls import path
from . import views

urlpatterns = [
    path('site/', views.site, name='site'),
    path('signup/', views.SignUp.as_view(), name='signup')
]
