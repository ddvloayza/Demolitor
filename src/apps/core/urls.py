from django.urls import path

from apps.core.views import Error404View, NosotrosView

from .views import (
    HomeView,
    ProductDetailView,
    ProductListView,
    ContactView,
    search_results,
    CategoryListView,
    CategoryDetailView
    )

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("nosotros/", NosotrosView.as_view(), name="nosotros"),
    path('product/<uuid:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('category/<uuid:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/', search_results, name='search_results'),
    path("404/", Error404View.as_view(), name="error-404"),
]
