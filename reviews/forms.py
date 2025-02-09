from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']  # Исключаем поле user_name из отображения
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
