from django.urls import path
from . import views

urlpatterns =[
    path('joinus/', views.JoinUsView.as_view(), name="join_us")
]