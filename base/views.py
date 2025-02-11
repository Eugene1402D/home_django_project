from django.shortcuts import render  # render используется для отображения шаблонов
from .models import SpecialOffer, GalleryImage  # SpecialOffer и GalleryImage импортируются из моделей для работы с данными базы данных


# функция обрабатывает запросы на главную страницу
def home(request):
    special_offers = SpecialOffer.objects.all()  # Извлекает все объекты SpecialOffer из базы данных и сохраняет их в переменную special_offers
    gallery_images = GalleryImage.objects.all()  # Извлекает все объекты GalleryImage из базы данных и сохраняет их в переменную gallery_images
    # словарь context, содержащий специальные предложения и изображения галереи, которые будут переданы в шаблон
    context = {
        "special_offers": special_offers,
        "gallery_images": gallery_images,
    }
    return render(request, "base/home.html", context)  # Использует render для отображения шаблона home.html и передачи в него контекста


# функция обрабатывает запросы на страницу специальных предложений
def special_offers(request):
    special_offers = SpecialOffer.objects.all()  # Извлекает все объекты SpecialOffer из базы данных и сохраняет их в переменную special_offers
    return render(
        request, "base/special_offers.html", {"special_offers": special_offers}
    )  # Использует render для отображения шаблона special_offers.html и передачи в него контекста


def gallery(request):
    gallery_images = GalleryImage.objects.all()  # Извлекает все объекты GalleryImage из базы данных и сохраняет их в переменную gallery_images
    # словарь context, содержащий специальные предложения и изображения галереи, которые будут переданы в шаблон
    context = {
        "gallery_images": gallery_images,
    }
    return render(request, "base/gallery.html",
                  context)
