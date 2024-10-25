from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

from apps.company.models import Company
from apps.product.models.product import Category
from apps.customuser.models.customuser import Banner


from apps.product.models.product import Product




def webpage_processor(request):
    # Calculate or fetch some dynamic data
    webpage_data = Company.objects.filter(comercial_name__icontains="demolitor").first()

    # Create a dictionary of values to be added to the context
    print("webpage_data", webpage_data)
    context = {
        'dynamic_data': webpage_data,
        'static_data': 'Hello, World!'
    }
    return context

class HomeView(TemplateView):
    template_name = "core/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ofertas'] = Product.objects.filter(
            category__company__comercial_name__icontains="demolitor",
            tag__slug="ofertas"
        )
        context['novedades'] = Product.objects.filter(
            category__company__comercial_name__icontains="demolitor",
            tag__slug="novedades"
        )
        context['packs'] = Product.objects.filter(
            category__company__comercial_name__icontains="demolitor",
            tag__slug="packs"
        )
        context['banners'] = Banner.objects.filter(first_slider=True)
        context['middle_banner'] = Banner.objects.filter(second_slider=True).first()
        print("middle_banner", context['middle_banner'])
        print("context['ofertas']", context['ofertas'])
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrar por búsqueda (categoría)
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(category__slug__icontains=search_query)

        # Filtrar por rango de precios
        price_range = self.request.GET.get('priceRange')
        if price_range:
            queryset = queryset.filter(price__lte=price_range)
            print("queryset", queryset)
        # Ordenar por
        sort_by = self.request.GET.get('sort_by')
        if sort_by == 'best_selling':
            queryset = queryset.order_by('-sales')  # Ajusta según tu modelo
        elif sort_by == 'highest_rated':
            queryset = queryset.order_by('-rating')  # Ajusta según tu modelo
        elif self.request.GET.get('price_order') == 'low_to_high':
            queryset = queryset.order_by('price')
        elif self.request.GET.get('price_order') == 'high_to_low':
            queryset = queryset.order_by('-price')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['categories'] = Category.objects.filter(is_active=True)
        context['total_count'] = paginator.count
        return context
    

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'core/category_detail.html'
    context_object_name = 'category'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        print("self.object_list", self.object.get_products)
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object.get_products, self.paginate_by)
        
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['total_count'] = paginator.count
        return context
    

class CategoryListView(ListView):
    model = Category
    template_name = 'core/category_list.html'
    context_object_name = 'categories'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        print("search_query", search_query)
        if search_query:
            queryset = queryset.filter(slug__icontains=search_query)
            print("queryset", queryset)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['products'] = self.object_list
        context['total_count'] = paginator.count
        return context


class Error404View(TemplateView):
    template_name = "core/errors/404.html"


def search_results(request):
    search_query = request.GET.get('search')
    results = []
    if search_query:
        results = Product.objects.filter(name__icontains=search_query)

    data = [{'name': product.name, 'uuid': product.uuid} for product in results]
    return JsonResponse(data, safe=False)

class ContactView(TemplateView):
    template_name = "core/contact.html"



