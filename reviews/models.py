from django.db import models


class Review(models.Model):
    user_name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    review_text = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(verbose_name="Оценка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # auto_now_add=True - устанавливает текущую дату и время при создании объекта

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.user_name} - {self.rating}"
