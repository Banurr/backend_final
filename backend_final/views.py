from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})
