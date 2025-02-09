# Generated by Django 4.2.1 on 2025-02-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="galleryimage",
            options={
                "verbose_name": "Изображение галереи",
                "verbose_name_plural": "Изображения галереи",
            },
        ),
        migrations.AlterModelOptions(
            name="sitemap",
            options={
                "verbose_name": "Карта сайта",
                "verbose_name_plural": "Карты сайта",
            },
        ),
        migrations.AlterModelOptions(
            name="specialoffer",
            options={
                "verbose_name": "Специальное предложение",
                "verbose_name_plural": "Специальные предложения",
            },
        ),
        migrations.AlterField(
            model_name="galleryimage",
            name="description",
            field=models.TextField(verbose_name="Описание изображения"),
        ),
        migrations.AlterField(
            model_name="galleryimage",
            name="image",
            field=models.ImageField(upload_to="gallery/", verbose_name="Изображение"),
        ),
        migrations.AlterField(
            model_name="galleryimage",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Название изображения"),
        ),
        migrations.AlterField(
            model_name="sitemap",
            name="section_name",
            field=models.CharField(max_length=200, verbose_name="Название раздела"),
        ),
        migrations.AlterField(
            model_name="sitemap",
            name="section_url",
            field=models.URLField(verbose_name="Ссылка на раздел"),
        ),
        migrations.AlterField(
            model_name="specialoffer",
            name="description",
            field=models.TextField(verbose_name="Описание акции"),
        ),
        migrations.AlterField(
            model_name="specialoffer",
            name="end_date",
            field=models.DateField(verbose_name="Дата окончания"),
        ),
        migrations.AlterField(
            model_name="specialoffer",
            name="image",
            field=models.ImageField(
                upload_to="special_offers/", verbose_name="Изображение акции"
            ),
        ),
        migrations.AlterField(
            model_name="specialoffer",
            name="start_date",
            field=models.DateField(verbose_name="Дата начала"),
        ),
        migrations.AlterField(
            model_name="specialoffer",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Название акции"),
        ),
    ]
