"""dreamer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include,path

from django.conf import settings
from django.conf.urls.static import static

# Admin Panel Customaization
admin.site.site_header='Dreamer Coaching Center'
admin.site.site_title='Dreamer Coaching Center'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('dj_rest_auth.urls')),

    path('api/attendances/', include('attendances.urls')),
    path('api/exams/', include('exams.urls')),
    path('api/profile/', include('profiles.urls')),
    path('api/materials/', include('materials.urls')),
    path('api/classes/', include('classes.urls')),
    path('api/timetable/', include('timetables.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)