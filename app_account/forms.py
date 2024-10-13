from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Profile,Address
from django.core.exceptions import ValidationError

user = get_user_model()

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = user
        fields = ('username', 'email', 'password1', 'password2')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'national_id', 'image']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['postal_code', 'description']

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور فعلی")
    new_password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور جدید")
    confirm_new_password = forms.CharField(widget=forms.PasswordInput, label="تکرار رمز عبور جدید")

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        current_password = self.cleaned_data.get('current_password')
        if not self.user.check_password(current_password):
            raise ValidationError("رمز عبور فعلی اشتباه است.")
        return current_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password != confirm_new_password:
            raise ValidationError("رمز عبور جدید و تکرار آن یکسان نیستند.")

        return cleaned_data