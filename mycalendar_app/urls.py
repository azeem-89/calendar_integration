# urls.py
from django.urls import path
from .views import  create_event,home,login,logout,create_event_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('create-event/', create_event_view, name='create_event'),
]
