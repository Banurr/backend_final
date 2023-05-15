from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect
from .form import MediaFileForm, RegistrationForm, ProfileForm, LoginForm,FilterForm
from .models import Product, Category, Comment, UserProfile

def index(request):
    user = request.user
    return render(request, 'base.html', {'user': user})
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
    curmin = 0
    curmax = 100000
    form = FilterForm(request.GET)
    arr = []
    res = []
    if form.is_valid():
        curmin = form.cleaned_data['minprice'] or 0
        curmax = form.cleaned_data['maxprice'] or 1000000
        filt = form.cleaned_data['Sortby'] or 'Ascen'
        for i in products:
            if curmin <= i.price <= curmax:
                arr.append((i, i.price,i.name))
        if filt == 'Ascen':
            arr.sort(key=lambda a: a[1], reverse=False)
        elif filt == 'Desc':
            arr.sort(key=lambda a: a[1], reverse=True)
        elif filt == 'Nameup':
            arr.sort(key=lambda a: a[2], reverse=False)
        elif filt == 'NameDown':
            arr.sort(key=lambda a: a[2], reverse=True)
        res = [p[0] for p in arr]
    content = {"all": res, "user": user, "categories": categories,"form":form}
    return render(request, 'allproducts.html', content)


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
    content = {"user": user, "categories": categories}
    return render(request, 'base.html', content)


def about_us(request):
    categories = Category.objects.all()
    user = request.user
    content = {"user": user, "categories": categories}
    return render(request, 'about_us.html', content)


def current_product(request, idx=1):
    categories = Category.objects.all()
    user = request.user
    product = get_object_or_404(Product, id=idx)
    comment = Comment.objects.filter(product=product)
    print(product)
    content = {"product": product, "comment": comment, "user": user, "categories": categories}
    return render(request, 'current_product.html', content)




def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():

            user = form.save()
            profile = UserProfile.objects.create(user=user,image=form.cleaned_data['image'])
            profile.save()
            return redirect('login')  # Replace 'home' with the URL name of your home page

    else:
        form = RegistrationForm()

    return render(request, 'retistration.html', {'form': form})


def login_view(request):
    form = LoginForm()
    user = request.user
    if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                content = {"user":user}
                return redirect('/',content)
            else:
                messages.info(request, 'Email or Username is incorrect!')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


def profile_view(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    categories = Category.objects.all()
    content = {"user" : user , "profile":profile,"categories":categories}
    return render(request, 'profile.html', content)

def search(request):
    t1 = request.GET.get("poisk")

    user = request.user
    categories = Category.objects.all()
    if t1:
        al = Product.objects.filter(name__icontains=t1)

    content = {
        'all': al,
        "user": user,
        "categories": categories
    }
    return render(request, 'Search_item.html', content)


def addbasket(request, idx):
    basket_list = request.session.get('basket', [])
    basket_list.append(idx)
    request.session['basket'] = basket_list
    return redirect('/')

def korzina(request):
    user = request.user
    categories = Category.objects.all()
    count=0
    total_price=0;
    if request.session['basket']:
        product_list=[]
        for id in request.session['basket']:
            product=Product.objects.filter(id=id)
            count=count+1
            for i in product:
                 total_price=total_price+i.price
                 product_list.append(i)

        content = {
            'all': product_list,
            'count':count,
            'total':total_price,
            "user": user,
            "categories": categories
        }
        return render(request,'korzina.html',content)
    else:
        return redirect('/')

