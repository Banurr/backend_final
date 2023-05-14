from django.shortcuts import render
from .form import MediaFileForm
from .models import Product,Category



def current_category(request, idx=1):
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=idx)
    products = Product.objects.filter(category=category)
    user = request.user
    content = {"categories": categories, "category": category, "products": products, "user": user}
    return render(request, 'current_category.html', content)


def allofthem(request):
    user = request.user
    products = Product.objects.all()
    categories = Category.objects.all()
    content = {"all": products, "user": user, "categories": categories}
    return render(request, 'allproducts.html', content)


    content = {"all": products, "user": user}
    return render(request,'allproducts.html',content)

# Create your views here.
def upload_media(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Perform checks or other operations on the uploaded image here
            return render(request, 'base.html')
    else:
        form = MediaFileForm()
    return render(request, 'upload.html', {'form': form})


def main(request):
    user = request.user
    categories = Category.objects.all()
    items = []
    r = 0
    for i in range(0, len(categories)):
        items.append(i)
    print(categories)
    # print(items)
    content = {"user": user, "categories": categories,"items": items}
    return render(request, 'base.html', content)


def about_us(request):
    categories = Category.objects.all()
    user = request.user
    return render(request, 'about_us.html', {"user": user, "categories": categories})


def current_product(request, idx):
    categories = Category.objects.all()
    user = request.user
    product = get_object_or_404(Product, id=idx)
    comment = Comment.objects.filter(product=product)
    print(product)
    content = {"product": product, "comment": comment, "user": user, "categories": categories}
    return render(request, 'current_product.html', content)

    return render(request, 'about_us.html', {"user":user})

