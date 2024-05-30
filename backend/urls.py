from django.contrib import admin
from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('blog/<str:slug>/', views.show, name="show"),
    path('creation/', views.creation, name="creation"),
    path('managearticle/', views.managearticle, name="managearticle"),
    path('blog/<str:slug>/modification/', views.modification, name="modification"),
    path('blog/<str:slug>/supprime/', views.supprime, name="supprime"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)