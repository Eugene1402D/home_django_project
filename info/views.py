from django.shortcuts import render


# Это представление обрабатывает запросы на страницу "О нас" (about)
def about(request):  # Функция about принимает объект запроса (request)
    return render(request, "info/about.html")  # Функция render отображает шаблон info/about.html


def contact(request):
    return render(request, "info/contact.html")


def faq(request):
    return render(request, "info/faq.html")
