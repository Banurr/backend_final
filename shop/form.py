from django import forms
from django.contrib.auth.models import User

from .models import Category, UserProfile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class MediaFileForm(forms.ModelForm):
    class Meta:
        model =Category
        fields = ('name', 'image')


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    image = forms.ImageField(required=False)
    # def clean_image(self):
    #     image = self.cleaned_data.get('image', False)
    #     if image:
    #         if image._size > 5 * 1024 * 1024:  # Adjust the file size limit if needed
    #             raise forms.ValidationError('Image file size must be less than 5MB.')
    #     return image


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {"password": {'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(validated_data['phone'], None, validated_data['password'])

            return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('image',)