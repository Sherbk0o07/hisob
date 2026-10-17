from django.urls import path
from .views import *
urlpatterns = [
    path('',home),
    path('<int:id>/',detail),
    path('create/book/view/',crate_book)
]