"""e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from accounts.views import index, logout, login, register, user_profile
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', all_products, name='index'),
    url(r'^index/', index, name="index"),
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
