from django.shortcuts import render
import requests
from django.db.models import Q
from django.shortcuts import render, redirect

from.models import Product

from django.core.paginator import Paginator

# Create your views here.
def index(request):
  return render(request,'index.html')

def product(request):
  contact_list = Product.objects.all()

  search_term=''

  if 'q' in request.GET:
        search_term = request.GET['q']
        contact_list = contact_list.filter(Q(name__icontains=search_term)).distinct()

  paginator = Paginator(contact_list, 20) # Show 4 contacts per page

  page = request.GET.get('page')
  products = paginator.get_page(page)
  return render(request, 'product.html', {'products': products})
