import shop
from . import views

from django.urls import path


urlpatterns = [
    path('', shop.views.allofthem, name='all'),
    path('<int:idx>', shop.views.current_product, name='current'),
    ]