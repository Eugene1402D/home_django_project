from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = UserLoginForm


@login_required
def profile(request):
    if request.method == 'POST':
        hotel_name = request.POST.get('hotel_name')
        room_type = request.POST.get('room_type')
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        user = request.user
        messages.success(request, 'Номер успешно забронирован!')
        return redirect('profile')
    return render(request, 'accounts/profile.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'accounts/update_profile.html', {'form': form})


@login_required
def book_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        user = request.user
        messages.success(request, 'Номер успешно забронирован!')
        return redirect('profile')
    return render(request, 'accounts/book_room.html')
