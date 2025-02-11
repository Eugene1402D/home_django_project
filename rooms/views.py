from django.shortcuts import render, get_object_or_404
from .models import Room


# представление обрабатывает запросы на страницу со списком номеров
def room_list(request):
    rooms = Room.objects.all()  # Извлекает все объекты модели Room из базы данных и сохраняет их в переменную rooms
    return render(request, "rooms/room_list.html", {"rooms": rooms})  # Отображает шаблон room_list.html, передавая в него контекст с номерами (rooms)


# представление обрабатывает запросы на страницу с деталями о конкретном номере
def room_detail(request, room_id):  # Функция room_detail принимает объект запроса (request) и идентификатор номера (room_id)
    room = get_object_or_404(Room, id=room_id)  # Извлекает объект модели Room по room_id из базы данных или возвращает ошибку 404, если объект не найден, и сохраняет его в переменную room
    return render(request, "rooms/room_detail.html", {"room": room})  # Отображает шаблон room_detail.html, передавая в него контекст с номером (room).
