from django.shortcuts import render


def about(request):
    return render(request, "info/about.html")


def contact(request):
    return render(request, "info/contact.html")


def faq(request):
    return render(request, "info/faq.html")
