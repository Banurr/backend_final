"""
URL configuration for backend_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import backend_final
import shop
from shop import views
from shop.views import upload_media
from backend_final import views, settings
from django.contrib import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop.views.main, name='home'),
<<<<<<< HEAD
    path('about_us', shop.views.about_us,name='about'),
    path('products/', include('shop.urls')),
=======
<<<<<<< HEAD
    path('about_us', shop.views.about_us, name='about'),
    path('category/<int:idx>', shop.views.current_category, name='currentc'),
    path('products/', include('shop.urls')),
=======
    path('about_us',shop.views.about_us,name='about'),
    path('products',shop.views.allofthem, name='all'),
>>>>>>> origin/main
>>>>>>> 9830b4f8d5a969755270e04ece85d31c6bb6807d
    path('upload/', upload_media, name='upload_media'),
    path('accounts/', include(('django.contrib.auth.urls', 'auth'), namespace='accounts')),
    path('accounts/profile/', backend_final.views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
