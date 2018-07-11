from django.urls import path

from . import views

app_name = "product"
urlpatterns = [
    path('', views.view_my_products, name='viewMyProducts'),
    path('<int:product_id>/', views.view_product, name='viewProduct'),
    path('edit/<int:product_id>', views.edit_product, name='editProduct'),
    path('create/', views.create_product, name='createProduct'),
    path('delete/<int:product_id>', views.delete_product, name='deleteProduct')
]
