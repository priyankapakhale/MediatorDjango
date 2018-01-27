"""mediator_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mediator_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add_user/',views.addUser),
    url(r'^get_user/',views.getUser),
    url(r'^add_medicine/', views.addMedicine),
    url(r'^get_medicine_records/', views.getMedicineRecords),
    url(r'^add_volunteer/', views.addVolunteer),
    url(r'^get_volunteer/', views.getVolunteer),
    url(r'^add_pickup_request/', views.addPickupRequst),

]
