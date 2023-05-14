<<<<<<< HEAD
import shop
=======
from django.conf.urls.static import static

import shop
from backend_final import settings
>>>>>>> 9830b4f8d5a969755270e04ece85d31c6bb6807d
from . import views

from django.urls import path


urlpatterns = [
    path('', shop.views.allofthem, name='all'),
<<<<<<< HEAD
    path('<int:idx>', shop.views.current_product, name='current'),
    ]
=======
    path('<int:idx>', shop.views.current_product, name='currentp'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

