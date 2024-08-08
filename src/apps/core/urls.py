from django.urls import path

from apps.core.views import Error404View

from .views import (
    HomeView,
    ProductDetailView,
    ProductListView,
    ContactView,
    CotizarView,
    CertificatesView,
    search_results,
    search_certificates,
    CategoryListView,
    CategoryDetailView
    )

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('products/<uuid:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('category/<uuid:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('cotizar/', CotizarView.as_view(), name='cotizar'),
    path('certificados/', CertificatesView.as_view(), name='certificados'),
    path('search/', search_results, name='search_results'),
    path('search-certificates/', search_certificates, name='search_certificates'),
    
    
    path("404/", Error404View.as_view(), name="error-404"),
]
