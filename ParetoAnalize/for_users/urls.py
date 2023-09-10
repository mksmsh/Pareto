from django.urls import path
from . import views


urlpatterns = [
    path('main', views.main, name='main'),
    path('profil', views.profil, name='profil'),
    path('product', views.product, name='product'),
    path('product/<int:shop_id>/', views.load_shop_data, name='load_shop_data'),
    path('clients', views.clients, name='clients'),
    path('competitor', views.competitor, name='competitor'),
    path('help', views.help, name='help'),
]
