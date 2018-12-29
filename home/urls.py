from django.urls import path
from home import views


urlpatterns = [
    path(r'/', views.home_page, name='home-page'),
    # path(r'/', views.home_page, name='home-page'),
]