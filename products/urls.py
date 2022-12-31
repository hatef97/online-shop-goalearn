from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name="product_list"),
    path('<int:pk>/', views.product_detail_view, name="product_detail"),
    path('add/', views.CreateNewProduct.as_view(), name="add_product"),
    path('<int:pk>/update', views.ProductUpdateView.as_view(), name='update_product'),
    path('<int:pk>/delete', views.ProductDeleteView.as_view(), name='delete_product')
]
