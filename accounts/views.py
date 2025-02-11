from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm


# представление обрабатывает регистрацию пользователей
def register(request):
    if request.method == 'POST':  # Если запрос является POST, он обрабатывает данные формы
        form = UserRegistrationForm(request.POST)
        if form.is_valid():  # Если форма действительна, она сохраняет нового пользователя и выполняет вход в систему
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправляет на домашнюю страницу после успешной регистрации
    else:
        form = UserRegistrationForm()  # Если запрос не является POST, он просто отображает форму регистрации
    return render(request, 'accounts/register.html', {'form': form})


# класс представления обрабатывает вход пользователей
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # и использует пользовательский шаблон (accounts/login.html)
    authentication_form = UserLoginForm  # и форму аутентификации (UserLoginForm).


# представление позволяет вошедшим пользователям управлять своим профилем и бронировать номера
@login_required
def profile(request):
    if request.method == 'POST':  # Если запрос является POST, он обрабатывает информацию о бронировании номера.
        hotel_name = request.POST.get('hotel_name')
        room_type = request.POST.get('room_type')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        user = request.user
        messages.success(request, 'Номер успешно забронирован!')  # Отображает сообщение об успешном бронировании
        return redirect('profile')  # и перенаправляет на страницу профиля.
    return render(request, 'accounts/profile.html')  # Если запрос не является POST, он просто отображает страницу профиля.


# представление обрабатывает обновление информации о профиле пользователя
@login_required
def update_profile(request):
    if request.method == 'POST':  # Если запрос является POST, он обрабатывает данные формы для обновления профиля пользователя
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():  # Если форма действительна, она сохраняет обновленный профиль и перенаправляет на страницу профиля
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)  # Если запрос не является POST, он отображает форму с текущей информацией о пользователе
    return render(request, 'accounts/update_profile.html', {'form': form})


# представление обрабатывает бронирование номеров вошедшими пользователями
@login_required
def book_room(request):
    if request.method == 'POST': # Если запрос является POST, он обрабатывает информацию о бронировании номера
        room_id = request.POST.get('room_id')
        user = request.user
        messages.success(request, 'Номер успешно забронирован!')  # Отображает сообщение об успешном бронировании и перенаправляет на страницу профиля
        return redirect('profile')
    return render(request, 'accounts/book_room.html')  # Если запрос не является POST, он просто отображает страницу бронирования номеров
