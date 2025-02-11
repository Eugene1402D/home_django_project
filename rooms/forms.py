from django import forms
from .models import Room


# форма основана на модели Room
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ["name", "description", "price", "image", "room_type"]  # fields: Указывает поля модели, которые должны быть включены в форму
