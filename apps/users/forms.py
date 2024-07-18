from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from apps.users.models import CustomUser


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )


class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )


class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, label='Phone Number')
    country_code = forms.ChoiceField(choices=[('+1', '+1 USA'), ('+7', '+7 Russia'), ('+7', '+7 Kazakhstan'),
                                              ('+375', '+375 Belarus'), ('+380', '+380 Ukraine'),
                                              ('+993', '+993 Turkmenistan'), ('+994', '+994 Azerbaijan'),
                                              ('+995', '+995 Georgia'), ('+996', '+996 Kyrgyzstan'),
                                              ('+998', '+998 Uzbekistan')], required=True, label='Country Code')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'country_code', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'country_code', 'profile_picture']


