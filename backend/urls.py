from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('blog/<str:slug>/', views.show, name="show"),
    path('creation/', views.creation, name="creation"),
]
