from django.shortcuts import render
from .models import Service


# Это представление обрабатывает запросы на страницу со списком услуг
def service_list(request):  # Функция service_list принимает объект запроса (request)
    services = Service.objects.all()  # Извлекает все объекты модели Service из базы данных и сохраняет их в переменную services
    return render(request, "services/service_list.html", {"services": services})
