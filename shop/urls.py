
import shop

from django.conf.urls.static import static

import shop
from backend_final import settings

from . import views

from django.urls import path

from .views import register

urlpatterns = [
    path('', shop.views.allofthem, name='all'),

    path('<int:idx>', shop.views.current_product, name='currentp'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

