from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание услуги")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, verbose_name="Цена"
    )
    image = models.ImageField(upload_to="services/", verbose_name="Изображение услуги")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name
