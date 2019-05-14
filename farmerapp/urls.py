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
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

schema_view = get_swagger_view(title='Farmerapp API')

urlpatterns = [
    url('', admin.site.urls),
    path('api/help',schema_view),
    path('api/farmer/',farmerviews.farmerList.as_view()),
    path('api/farmer/<int:pk>', farmerviews.farmerDetail.as_view()),
    path('api/farmer/<slug:cropGrown>',farmerviews.farmerQuery),
    path('api/farm/',farmviews.farmList.as_view()),
    path('api/farm/<int:pk>', farmviews.farmDetail.as_view()),
    path('api/farm/ownedby/<int:farmerId>', farmviews.farmQuery),
    path('api/fertilizer/',fertilizerviews.fertilizerList.as_view()),
    path('api/fertilizer/<int:pk>',fertilizerviews.fertilizerDetail.as_view()),
    path('api/schedule/',scheduleviews.scheduleList.as_view()),
    path('api/schedule/<int:pk>',scheduleviews.scheduleDetail.as_view()),
    path('api/schedule/due',scheduleviews.scheduleQuery),
    path('api/schedule/byfarm/<int:farmId>',scheduleviews.scheduleByFarm),
    path('api/billofmaterial/<int:farmerId>', billofmaterialviews.BillOfMaterial),
]