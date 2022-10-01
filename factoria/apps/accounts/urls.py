from django.urls import path
from . import views

urlpatterns = [
    path('list', views.ListClient, name='list'),
    path('update_view/<int:id>/', views.update_view, name='update_view'),
    path('client/<int:client_id>/', views.detail_product, name='client_detail_view'),
    path('<int:client_id>/delete/', views.delete_view, name='delete'),
    path('add', views.add_client, name='forms'),
    path('login', views.login_view, name='login'),
]