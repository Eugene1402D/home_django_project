from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm
from .models import Review


def review_list(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/review_list.html", context)


@login_required
@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_name = request.user.username  # Установка имени пользователя
            review.save()
            messages.success(request, 'Ваш отзыв успешно добавлен.')
            form = ReviewForm()  # Очистить форму после сохранения
        else:
            print(form.errors)  # Вывод ошибок формы для отладки
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user_name=request.user.username)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш отзыв успешно обновлен.')
            return redirect('review_list')  # Перенаправление на список отзывов после сохранения
        else:
            print(form.errors)  # Вывод ошибок формы для отладки
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/edit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user_name=request.user.username)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Ваш отзыв успешно удален.')
        return redirect('review_list')
    return render(request, 'reviews/delete_review.html', {'review': review})
