"""
URL configuration for owner project.

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
from django.contrib import admin
from django.urls import path

from customer import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name="index"),
    path('homeabout', views.homeabout, name="homeabout"),
    path('logcheck', views.logcheck, name="logcheck"),
    path('userreg', views.userreg, name="userreg"),
    path('insertbooking',views.insertbooking,name="insertbooking"),
    path('insertbuilder',views.insertbuilder,name="insertbuilder"),
    path('insertcustomer',views.insertcustomer,name="insertcustomer"),
    path('insertproject',views.insertproject,name="insertproject"),
    path('insertsite',views.insertsite,name="insertsite"),
    path('viewbooking',views.viewbooking,name="viewbooking"),
    path('viewbuilders',views.viewbuilders,name="viewbuilders"),
    path('viewcustomer',views.viewcustomer,name="viewcustomer"),
    path('viewproject',views.viewproject,name="viewproject"),
    path('viewsite',views.viewsite,name="viewsite"),
    path('sendmail',views.sendmail,name="sendmail"),
    path('changepassword',views.changepassword,name="changepassword"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
