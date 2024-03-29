"""Forms for users app"""
from allauth.account.forms import SignupForm, ResetPasswordKeyForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .widgets import SelectWithDisabled

SELECT_YOUR_RANK = [("", {"label": "Select Your Rank", "disabled": True})]


class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form for admin panel"""

    class Meta:
        model = CustomUser
        fields = "__all__"


class UserSignupForm(SignupForm):
    """Allauth Signup Form customized and extended"""

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields["email2"].widget.attrs["placeholder"] = "Confirm e-mail"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm password"

    username = forms.CharField(
        max_length=50,
        label="Username",
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    first_name = forms.CharField(
        max_length=30,
        label="First Name",
        widget=forms.TextInput(attrs={"placeholder": "First Name"}),
    )
    last_name = forms.CharField(
        max_length=30,
        label="Last Name",
        widget=forms.TextInput(attrs={"placeholder": "Last Name"}),
    )

    rank = forms.ChoiceField(
        label="Rank",
        choices=SELECT_YOUR_RANK + CustomUser.ROLES,
        widget=SelectWithDisabled(),
    )

    def save(self, request):
        print(self.cleaned_data)
        user = super(UserSignupForm, self).save(request)
        user.username = self.cleaned_data.get("username")
        user.save()
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.rank = self.cleaned_data.get("rank")
        user.is_active = self.cleaned_data.get("is_active")
        user.is_active = False
        user.save()
        return user


class EditProfileForm(forms.ModelForm):
    """Custom Edit Profile Form"""

    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "rank",
        )


class MyCustomResetPasswordKeyForm(ResetPasswordKeyForm):
    """Custom Password Reset Form to update a placeholder"""

    def __init__(self, *args, **kwargs):
        super(MyCustomResetPasswordKeyForm, self).__init__(*args, **kwargs)
        self.fields["password2"].widget.attrs["placeholder"] = "Repeat New Password"
