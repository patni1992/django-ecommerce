from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cart'

urlpatterns = [
    path('detail', views.detail, name='detail'),
    path('add/<int:product_id>/', views.add, name='add'),
    path('remove/<int:product_id>/', views.remove, name='remove'),
    path('update', views.update, name='update'),
]

