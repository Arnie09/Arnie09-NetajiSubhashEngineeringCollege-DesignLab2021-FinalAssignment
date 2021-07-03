"""ecommerce_cart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from ecommerce.views import index, load_products, checkout, checkout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homepage'),
    path('load_products/', load_products, name='load'),
    path('checkout/', checkout, name='checkout'),
    path('checkout_page/', checkout_page, name='checkout_page')
]
