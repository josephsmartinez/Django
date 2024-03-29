"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
#from pages import views
#from pages.views import home_view, contact_view, about_view, current_datetime_view, data_view, scaffolding_example_view  # This make things more explicit
#from products.views import product_detail_view, product_create_view

urlpatterns = [
    #path('home/', home_view, name='home'),
    #path('contact/', contact_view, name='contact'),
    #path('about/', about_view, name='about'),
    #path('datetime/', current_datetime_view, name='date_time'),
    #path('data/', data_view, name='data'),
    #path('products/', product_detail_view),
    #path('create/', product_create_view),
    #path('example/', scaffolding_example_view),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
