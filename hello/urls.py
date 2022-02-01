from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("jen", views.jen, name="jen"),
    path("<str:name>", views.greet, name="greet")
]