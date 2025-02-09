# Hotel Booking Website

## Описание
Это проект сайта для бронирования отелей, который позволяет пользователям искать и бронировать отели в различных
странах и городах. Сайт предоставляет информацию о номерах, услугах отеля, а также позволяет оставлять отзывы
и управлять бронированиями.

## Архитектура
Проект состоит из следующих приложений:

1. **base**: Главная страница сайта, включающая информацию о специальных предложениях, галерею фотографий и карту сайта.
2. **info**: Информационные страницы, включая разделы "О нас", "Контакты", "Часто задаваемые вопросы (FAQ)" и "Блог".
3. **services**: Услуги отеля, включая информацию о бассейне, спортзале, кинотеатре, массаже, бильярде, spa и других услугах.
4. **rooms**: Список доступных номеров с описанием и ценами, включая стандартные комнаты, семейные номера и номера с видом на море (горы, улицу, детскую площадку).
5. **reviews**: Отзывы посетителей, позволяющие оставлять отзывы и оценки для номеров и услуг.
6. **accounts**: Регистрация и личный кабинет, позволяющие пользователям регистрироваться, входить в личный кабинет, управлять бронированиями и обновлять личные данные.

## Система обновления информации

Информация на сайте обновляется следующими методами:
1. **Административная панель**: Администраторы могут вручную добавлять и редактировать информацию об отелях, номерах и услугах через административную панель Django.
2. **Импорт данных**: Скрипты для импорта данных из CSV или JSON файлов в базу данных Django.
3. **API интеграция**: Использование API отелей, таких как Booking.com, Expedia, Hotels.com и других, для получения актуальной информации об отелях, номерах и ценах.
4. **Формы для пользователей**: Формы на сайте, позволяющие пользователям оставлять отзывы и оценки.
5. **Синхронизация с внешними базами данных**: Настройка синхронизации данных между сайтом и внешними базами данных.

## Установка и запуск

1. Клонируйте репозиторий:
   git clone git@github.com:Eugene1402D/home_django_project.git
   cd hotel_booking

Установите зависимости:
pip install -r requirements.txt

Примените миграции:
python manage.py makemigrations
python manage.py migrate

Запустите сервер разработки:
python manage.py runserver

Контакты
Если у вас есть вопросы или предложения, свяжитесь с нами по адресу eugened1402@mail.ru.

Этот файл `README.md` предоставляет полное описание проекта, его архитектуры, системы обновления информации, а также инструкции по установке и запуску.
Если у вас есть еще вопросы или предложения, дайте знать!