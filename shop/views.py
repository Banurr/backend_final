from django.shortcuts import render
from .form import MediaFileForm
from .models import Product,Category



def allofthem(request):
    user = request.user
    products = Product.objects.all()
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
    user = request.user
    return render(request, 'about_us.html', {"user":user})
