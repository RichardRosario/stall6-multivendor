from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Vendor

def createVendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name=user.username, email=user.email, created_by=user)

            return redirect('frontpage')

    return render(request, 'vendor/create-vendor.html', {})


def vendorsList(request):
    vendors = Vendor.objects.all()

    context = {
        'vendors': vendors
    }

    return render(request, 'vendor/list.html', context)

