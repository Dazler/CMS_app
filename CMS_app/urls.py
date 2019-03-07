from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('a320.html/', views.A320, name = "A320"),
    path('a330.html/', views.A330, name = "A330"),
    path('a350.html/', views.A350, name = "A350"),
]