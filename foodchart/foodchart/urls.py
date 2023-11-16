"""foodchart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from dishes.views import *
from .urls import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("services/", services, name="services"),
    path("contacts/", contacts, name="contacts"),
    path("add-dishes/", add_dishes, name="add_dishes"),
    path("show-dishes/", show_dishes, name="show_dishes"),
    path("order-food/", order_food, name="order-food"),
    path("delete-dish/<int:id>/", delete_dish, name="delete-dish"),
    path("update-dish/<int:id>/", update_dish, name="update-dish"),
    path("login/", login_page, name="login_page"),
    path("register/", register_page, name="register_page"),
    path("logout/", logout_page, name="logout_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
