from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm
from .models import Review


# представление отображает список всех отзывов
def review_list(request):
    reviews = Review.objects.all()  # Получает все объекты модели Review из базы данных и сохраняет их в переменную reviews
    context = {
        "reviews": reviews,
    }  # Создает контекст context, содержащий отзывы
    return render(request, "reviews/review_list.html", context)  # тображает шаблон review_list.html, передавая в него контекст с отзывами


# представление обрабатывает добавление нового отзыва
@login_required  # Декоратор @login_required требует аутентификации для доступа к представлению
def add_review(request):
    if request.method == 'POST':  # Если запрос является POST, обрабатывает данные формы ReviewForm
        form = ReviewForm(request.POST)
        if form.is_valid():  # Если форма действительна
            review = form.save(commit=False)  #  то создает объект отзыва
            review.user_name = request.user.username  # установка имени пользователя
            review.save()  # и сохраняет отзыв
            messages.success(request, 'Ваш отзыв успешно добавлен.')  # Отображает сообщение об успешном добавлении отзыва
            form = ReviewForm()  # Очистить форму после сохранения
        else:
            print(form.errors)  # Вывод ошибок формы для отладки
    else:
        form = ReviewForm()  # Если запрос не является POST, отображает пустую форму
    return render(request, 'reviews/add_review.html', {'form': form})


# представление обрабатывает редактирование существующего отзыва
@login_required  # Декоратор @login_required требует аутентификации для доступа к представлению
def edit_review(request, review_id):  # Получает объект отзыва по review_id и имени пользователя или возвращает ошибку 404, если отзыв не найден
    review = get_object_or_404(Review, id=review_id, user_name=request.user.username)
    if request.method == 'POST':  # Если запрос является POST, обрабатывает данные формы ReviewForm для обновления отзыва
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():  # Если форма действительна, сохраняет изменения и отображает сообщение об успешном обновлении
            form.save()
            messages.success(request, 'Ваш отзыв успешно обновлен.')
            return redirect('review_list')  # Перенаправление на список отзывов после сохранения
        else:
            print(form.errors)  # Вывод ошибок формы для отладки
    else:
        form = ReviewForm(instance=review)  # Если запрос не является POST, отображает форму с текущими данными отзыва
    return render(request, 'reviews/edit_review.html', {'form': form})


# представление обрабатывает удаление существующего отзыва
@login_required  # Декоратор @login_required требует аутентификации для доступа к представлению
def delete_review(request, review_id):  # Получает объект отзыва по review_id и имени пользователя или возвращает ошибку 404, если отзыв не найден
    review = get_object_or_404(Review, id=review_id, user_name=request.user.username)
    if request.method == 'POST':  # Если запрос является POST, удаляет отзыв и отображает сообщение об успешном удалении
        review.delete()
        messages.success(request, 'Ваш отзыв успешно удален.')
        return redirect('review_list')  # Перенаправляет на список отзывов после успешного удаления
    return render(request, 'reviews/delete_review.html', {'review': review})  # Если запрос не является POST, отображает шаблон подтверждения удаления отзыва.
