"""ecomsite URL Configuration

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
from shop.views import index, ByPriceAes, ByPriceDes, AZ, ZA
from userprofile.views import signup
from shop.views import detail ,checkout,orderconfirm
from django.contrib.auth import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('<int:id>/',detail,name='detial'),
    path('bypriceaes/',ByPriceAes,name='ByPriceAes'),
    path('bypricedes/',ByPriceDes,name='ByPriceDes'),
    path('a-z/',AZ,name='AZ'),
    path('z-a/',ZA,name='ZA'),
    path('checkout/',checkout,name='checkout'),
    path('orderconfirm/',orderconfirm,name='orderconfirm'),
    path('signup/',signup,name='signup'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('login/',views.LoginView.as_view(template_name='login.html'),name='login'),
]
