"""farmerapp URL Configuration

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
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from farmer import views as farmerviews
from farm import views as farmviews
from fertilizer import views as fertilizerviews
from schedule import views as scheduleviews
from billofmaterial import views as billofmaterialviews
from userprofile import views as userprofileviews
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
schema_view = get_swagger_view(title='Farmerapp API')

urlpatterns = [
    path('', schema_view),
    url('accounts/',admin.site.urls),
    path('farmer/',farmerviews.farmerList.as_view()),
    path('farmer/<int:pk>', farmerviews.farmerDetail.as_view()),
    path('farmer/<slug:cropGrown>',farmerviews.farmerQuery),
    path('farm/',farmviews.farmList.as_view()),
    path('farm/<int:pk>', farmviews.farmDetail.as_view()),
    path('farm/ownedby/<int:farmerId>', farmviews.farmQuery),
    path('fertilizer/',fertilizerviews.fertilizerList.as_view()),
    path('fertilizer/<int:pk>',fertilizerviews.fertilizerDetail.as_view()),
    path('schedule/',scheduleviews.scheduleList.as_view()),
    path('schedule/<int:pk>',scheduleviews.scheduleDetail.as_view()),
    path('schedule/due',scheduleviews.scheduleQuery),
    path('schedule/byfarm/<int:farmId>',scheduleviews.scheduleByFarm),
    path('userprofile/<slug:country>', userprofileviews.userprofileUpdate),
    path('billofmaterial/<int:farmerId>', billofmaterialviews.BillOfMaterial),
]