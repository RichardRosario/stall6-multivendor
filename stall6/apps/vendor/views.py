from django.shortcuts import render, get_object_or_404

from .models import Vendor

def vendorslist(request):
    vendors = get_object_or_404(Vendor, )

    context = {
        'vendors': vendors
    }

    return render(request, 'frontpage.html', context)