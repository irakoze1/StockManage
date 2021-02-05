from django.contrib import admin
from django.urls import path
from stockmanagment import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_items/', views.list_items, name='list_items'),
    path('add_items/', views.add_items, name='add_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('admin/', admin.site.urls),
]
