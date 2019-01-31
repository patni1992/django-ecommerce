from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'order'

urlpatterns = [
    path('load-cities/', views.load_cities, name='load_cities'),
    path('', views.order, name='order'),
]
