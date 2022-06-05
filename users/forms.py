"""Forms for users app"""
from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form for admin panel"""
    class Meta:
        model = CustomUser
        fields = "__all__"

class UserSignupForm(SignupForm):
    """Allauth Signup Form extended"""
    username = forms.CharField(
        max_length=50,
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    first_name = forms.CharField(
        max_length=30,
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    phone = forms.CharField(
        max_length=30,
        label='Phone Number',
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number'})
    )
    rank = forms.IntegerField(widget=forms.HiddenInput(), initial=5)

    def save(self, request):
        print(self.cleaned_data)
        user = super(UserSignupForm, self).save(request)
        user.phone = self.cleaned_data.get('phone')
        user.username = self.cleaned_data.get('username')
        user.save()
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.role = self.cleaned_data.get('role')
        user.save()
        return user