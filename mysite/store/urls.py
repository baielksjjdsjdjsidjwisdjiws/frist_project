from .views import (ProductlistViews, ProductDetailViews,
                    ProductCreatViews, ProductUpdateViews, ProductDeleteViews)
from django.urls import path



urlpatterns = [
    path('', ProductlistViews.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailViews.as_view(), name='product_detail'),
    path('create/', ProductCreatViews.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateViews.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteViews.as_view(), name='product_delete')
]