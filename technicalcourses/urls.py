from django.urls import path
from . import views

urlpatterns = [
    path('<int:course_id>/', views.details, name='details-page'),
    path('', views.courses, name= 'home-page'),
]
