from django.shortcuts import render
from .models import SpecialOffer, GalleryImage


def home(request):
    special_offers = SpecialOffer.objects.all()
    gallery_images = GalleryImage.objects.all()
    context = {
        "special_offers": special_offers,
        "gallery_images": gallery_images,
    }
    return render(request, "base/home.html", context)


def special_offers(request):
    special_offers = SpecialOffer.objects.all()
    return render(
        request, "base/special_offers.html", {"special_offers": special_offers}
    )


def gallery_list(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, "base/gallery_list.html", {"gallery_images": gallery_images})

