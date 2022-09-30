from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import DetailView, ListView

from products.models import Products, Category


class ProductDetails(DetailView):
    template_name = 'product-detail.html'
    model = Products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Products.objects.get(pk=self.kwargs.get('pk'))
        return context


class CategoryDetail(View):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        products = Products.objects.filter(category=category)
        context = {
            'products': products,
            'category': category,
        }
        return render(request, 'Category_Detail.html', context)


class ProductsPage(ListView):
    template_name = 'products.html'
    model = Products
    context_object_name = 'product'
    paginate_by = 2
    ordering = '-id'
