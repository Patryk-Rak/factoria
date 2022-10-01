from django.urls import path, include
from . import views


app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_product/', views.add_from, name='form'),
    path('list/', views.list_view, name='list_view'),
    path('update_view/<int:id>/', views.update_view, name='update_view'),
    path('product/<int:product_id>/', views.detail_product, name='product_detail_view'),
    path('<int:product_id>/delete/', views.delete_view, name='delete'),
]
