from django.shortcuts import render,redirect,get_object_or_404

from shop.forms import Orderform
from .models import Order, Products, PostImage
from django.core.paginator import Paginator

# Create your views here.


def index(request):
  product_objects = Products.objects.all()
  
  
  item_name = request.GET.get('item_name')
  if item_name!= '' and item_name is not None:
    product_objects = product_objects.filter(title__icontains=item_name)
    
  
  paginator = Paginator(product_objects,12)
  page = request.GET.get('page')
  product_objects = paginator.get_page(page)
  
  return render(request,'shop/index.html',{'product_objects':product_objects})

def ByPriceAes(request):
  product_objects = Products.objects.order_by('price')
  
  
  item_name = request.GET.get('item_name')
  if item_name!= '' and item_name is not None:
    product_objects = product_objects.filter(title__icontains=item_name)
    
  
  paginator = Paginator(product_objects,12)
  page = request.GET.get('page')
  product_objects = paginator.get_page(page)
  
  return render(request,'shop/bypriceAes.html',{'product_objects':product_objects})

def ByPriceDes(request):
  product_objects = Products.objects.order_by('-price')
  
  
  item_name = request.GET.get('item_name')
  if item_name!= '' and item_name is not None:
    product_objects = product_objects.filter(title__icontains=item_name)
    
  
  paginator = Paginator(product_objects,12)
  page = request.GET.get('page')
  product_objects = paginator.get_page(page)
  
  return render(request,'shop/bypriceDes.html',{'product_objects':product_objects})

def AZ(request):
  product_objects = Products.objects.order_by('title')
  
  
  item_name = request.GET.get('item_name')
  if item_name!= '' and item_name is not None:
    product_objects = product_objects.filter(title__icontains=item_name)
    
  
  paginator = Paginator(product_objects,12)
  page = request.GET.get('page')
  product_objects = paginator.get_page(page)
  
  return render(request,'shop/A-Z.html',{'product_objects':product_objects})

def ZA(request):
  product_objects = Products.objects.order_by('-title')
  
  
  item_name = request.GET.get('item_name')
  if item_name!= '' and item_name is not None:
    product_objects = product_objects.filter(title__icontains=item_name)
    
  
  paginator = Paginator(product_objects,12)
  page = request.GET.get('page')
  product_objects = paginator.get_page(page)
  
  return render(request,'shop/Z-A.html',{'product_objects':product_objects,})

def detail(request,id):
  product_object = Products.objects.get(id=id)

  return render(request,'shop/detail.html',{'product_object':product_object})


def checkout(request):
  #if request.method == "POST":
    
    #items = request.POST.get('items',"")
    #name = request.POST.get('name',"")
    #email = request.POST.get('email',"")
    #address = request.POST.get('address',"")
    #state = request.POST.get('state',"")
    #zipcode = request.POST.get('zipcode',"")
    #city = request.POST.get('city',"")
    #total = request.POST.get('total',"")
    #order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
    #order.save()   
     
  #return render(request,'shop/checkout.html')

  if request.method == "GET":
    order_form = Orderform()
  else:
    order_form = Orderform(request.POST)
    if order_form.is_valid():
      items = request.POST.get('items',"")
      name = request.POST.get('name',"")
      email = request.POST.get('email',"")
      address = request.POST.get('address',"")
      state = request.POST.get('state',"")
      zipcode = request.POST.get('zipcode',"")
      city = request.POST.get('city',"")
      total = request.POST.get('total',"")
      order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
      order.save()  
      return redirect('orderconfirm') 
       
    
      
  return render(request,'shop/checkout.html',{
    'form':order_form,
  })


def orderconfirm(request):
  return render(request,'shop/order.html')