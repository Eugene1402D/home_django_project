from django import forms
from .models import Review


# класс используется для создания формы, которая позволяет пользователям отправлять отзывы
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # model: Указывает, что форма основана на модели Review
        fields = ['review_text', 'rating']  # Исключаем поле user_name из отображения
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }  # используется NumberInput для поля rating, которое задает минимальное и максимальное значения оценки (от 1 до 5)
