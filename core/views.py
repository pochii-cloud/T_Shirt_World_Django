from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from core.models import Contact
from products.models import Products, Category


class Homepage(View):
    def get(self, request):
        product = Products.objects.all()
        categories = Category.objects.all()
        context = {'product': product,
                   'categories': categories
                   }
        return render(request, 'index.html', context)


class Navigation(TemplateView):
    template_name = 'nav.html'


class Footer(TemplateView):
    template_name = 'footer.html'


class AboutUs(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactUs(View):
    def get(self, request):
        categories = Category.objects.all()
        categories = Category.objects.all()
        context = {
                   'categories': categories
                   }
        return render(request, 'contact.html',context)

    def post(self, request):
        contact = Contact()
        contact.save_contacts(request=request)
        return render(request, 'contact.html')


class SearchResults(View):
    def get(self, request):
        search = request.GET.get('search')
        product = Products.objects.all().filter(name__icontains=search).order_by('name')
        context = {'product': product}
        return render(request,'SearchResults.html',context)