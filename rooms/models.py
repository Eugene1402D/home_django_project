from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название номера")
    description = models.TextField(verbose_name="Описание номера")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за ночь"
    )
    image = models.ImageField(upload_to="rooms/", verbose_name="Изображение номера")
    room_type = models.CharField(max_length=100, verbose_name="Тип номера")

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"

    def __str__(self):
        return self.name
