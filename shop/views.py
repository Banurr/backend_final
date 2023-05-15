from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404, redirect
from .form import MediaFileForm, RegistrationForm, ProfileForm, LoginForm
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
    content = {"all": products, "user": user, "categories": categories}
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
    user=request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.userprofile)
        profile=UserProfile(request.POST);
        content = {"user":user,"form":form,"profilr":profile}
    return render(request, 'profile.html', content)

def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    booki = set()
    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            booki = Book.objects.filter(title__icontains=search)
        else:
            first_name_contributor = Contributor.objects.filter(first_names__icontains=search)

            for contributor in first_name_contributor:
                for book in contributor.book_set.all():
                    booki.add(book)

            last_name_contributor = Contributor.objects.filter(last_names__icontains=search)

            for contributor in last_name_contributor:
                for book in contributor.book_set().all():
                    booki.add(book)

        if request.user.is_authenticated:
            search_history.append([search, search_in])
            request.session['search_history'] = search_history
        elif search_history:
            initial = dict(search=search_text, search_in=search_history[-1][0])
            form = SearchForm(initial=initial)

    return render(request, "search_results.html", {"form": form, "search_text": search_text, "books": booki})