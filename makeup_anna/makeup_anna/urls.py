from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views

urlpatterns = [
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
]

