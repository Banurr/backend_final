from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class ShopAdminConfig(AdminConfig):
    default_site = 'sadmin.admin.ShopAdmin'
