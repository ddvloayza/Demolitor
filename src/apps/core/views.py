from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from django.views.generic.detail import DetailView

from apps.company.models import Company
from apps.product.models.product import Category
from apps.customuser.models.customuser import CustomWebPage, Banner
from django.db.models import Prefetch

from apps.product.models.product import Product, Certificate
from django.db.models import Q



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
        context['banners'] = Banner.objects.all()
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
        search_query = self.request.GET.get('search')
        print("search_query", search_query)
        if search_query:
            queryset = queryset.filter(category__slug__icontains=search_query)
            print("queryset", queryset)
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

class CotizarView(TemplateView):
    template_name = "core/cotizar.html"


class CertificatesView(TemplateView):
    template_name = "core/certificados.html"


def search_certificates(request):
    search_lote = request.GET.get('lote')
    search_product = request.GET.get('product')
    query = Q()
    if search_product:
        query &= Q(code__icontains=search_product)
    if search_lote:
        query &= Q(lote__icontains=search_lote)

    results = Certificate.objects.filter(query)

    data = [
        {
            'name': certificate.product.name,
            'uuid': certificate.product.uuid,
            'certificate': certificate.certificado.url
        }
        for certificate in results
    ]
    return JsonResponse(data, safe=False)