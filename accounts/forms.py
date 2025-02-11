from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# класс используется для создания формы регистрации пользователя
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # widget=forms.PasswordInput (использует виджет PasswordInput для отображения скрытого ввода пароля)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User  # model: Указывает, что форма основана на модели User
        fields = ["username", "email", "password"]

    def clean_password2(self):  # Проверяет, совпадают ли значения полей password и password2
        cd = self.cleaned_data  # Получает очищенные данные из формы
        if cd["password"] != cd["password2"]:  # Если пароли не совпадают, поднимает ошибку валидации
            raise forms.ValidationError("Пароли не совпадают.")
        return cd["password2"]  # Возвращает значение поля password2, если проверка прошла успешно


# класс используется для создания формы аутентификации (входа в систему) пользователя
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя")  # label="Имя пользователя" (читаемое имя для поля)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
