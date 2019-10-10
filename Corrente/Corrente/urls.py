from django.contrib import admin
from django.urls import path, include
from webApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('consumo/', views.consumeList.as_view()),
    path('webapp/',include('webApp.url')),
]
