from django import forms
from django.contrib.auth.models import User

from .models import Category, UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class MediaFileForm(forms.ModelForm):
    class Meta:
        model =Category
        fields = ('name', 'image')


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

    image = forms.ImageField(required=False)

    # def clean_image(self):
    #     image = self.cleaned_data.get('image', False)
    #     if image:
    #         if image._size > 5 * 1024 * 1024:  # Adjust the file size limit if needed
    #             raise forms.ValidationError('Image file size must be less than 5MB.')
    #     return image

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image',)