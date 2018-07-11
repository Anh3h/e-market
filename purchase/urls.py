from django.urls import path

from . import views

app_name = "purchase"
urlpatterns = [
    path('?product_id=<int:product_id>', views.create_transaction, name='createTransaction')
]
