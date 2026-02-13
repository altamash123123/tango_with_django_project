from django.shortcuts import render
from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': 'Rango is awesome!'}
    return render(request, 'rango/about.html', context=context_dict)
