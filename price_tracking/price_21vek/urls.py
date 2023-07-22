from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('update/', updates, name='update'),
    path('products/<slug:product_slug>/', product_price, name = 'product'),
    path('<slug:catalog_slug>/', catalogy, name = 'catalog'),



]

