# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def doula_description(request):
    return render(request, 'doula/description.html', {})


def doula_services(request):
    return render(request, 'doula/services.html', {})


def photo_gallery(request):
    return render(request, 'photo/gallery.html', {})


def photo_price(request):
    return render(request, 'photo/price.html', {})


def yoga_class(request):
    return render(request, 'yoga/class.html', {})


def yoga_locations(request):
    return render(request, 'yoga/locations.html', {})


def yoga_price(request):
    return render(request, 'yoga/price.html', {})


def yoga_schedule(request):
    return render(request, 'yoga/schedule.html', {})


