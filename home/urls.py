from django.urls import path
from home import views


urlpatterns = [
    path(r'/', views.home_page, name='home-page'),
    path(r'/thanks.html', views.thanks_page, name='thanks-page'),
    path(r'/resulat.html', views.resultat_page, name='resultat-page'),
]