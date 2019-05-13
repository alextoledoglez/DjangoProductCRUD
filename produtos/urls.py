from django.urls import path

from .views import product_list, product_new, product_update, product_delete

urlpatterns = [
    path('list/', product_list, name="product_list"),
    path('new/', product_new, name="product_new"),
    path('update/<int:id>/', product_update, name="product_update"),
    path('delete/<int:id>/', product_delete, name="product_delete"),
]
