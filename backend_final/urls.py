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
from shop.views import upload_media, register, login_view, logout_view, profile_view, search,addbasket,korzina,payment
from backend_final import views, settings
from django.contrib import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop.views.main, name='home'),
    path('about_us', shop.views.about_us, name='about'),
    path('category/<int:idx>', shop.views.current_category, name='currentc'),
    path('products/', include('shop.urls')),
    path('upload/', upload_media, name='upload_media'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('search/', search,name='search'),
    path('addbasket/<int:idx>', addbasket,name='addbasket'),
    path('korzina/', korzina,name='korzina'),
    path('pay/<int:total>',payment,name='pay'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
