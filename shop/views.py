from django.shortcuts import render


from store.models import Product

def frontpage(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:6]

    return render(request, 'shop/frontpage.html', {
        'products': products
    })

def about(request):
    return render(request, 'shop/about.html')



