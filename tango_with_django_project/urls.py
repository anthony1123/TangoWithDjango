
from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views

#c4
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name='index'),
    # chapter 3
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls)
#c4
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
