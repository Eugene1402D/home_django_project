from django.db import models


class SpecialOffer(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название акции")
    description = models.TextField(verbose_name="Описание акции")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    image = models.ImageField(
        upload_to="special_offers/", verbose_name="Изображение акции"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Специальное предложение"
        verbose_name_plural = "Специальные предложения"
        ordering = ["title"]


class GalleryImage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название изображения")
    description = models.TextField(verbose_name="Описание изображения")
    image = models.ImageField(upload_to="gallery/", verbose_name="Изображение")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Изображения галереи"


class SiteMap(models.Model):
    section_name = models.CharField(max_length=200, verbose_name="Название раздела")
    section_url = models.URLField(verbose_name="Ссылка на раздел")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Карта сайта"
        verbose_name_plural = "Карты сайта"
