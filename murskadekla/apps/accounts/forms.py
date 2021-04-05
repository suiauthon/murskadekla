from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import EmailActivation
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.urls import reverse
from django.utils.safestring import mark_safe

class LoginForm(forms.Form):
    email    = forms.EmailField(label='Email')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "nesto",
                                          "id": "nesto1"})
    )

class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            user = get_user_model().objects.get(email=email)
            print(user)
        except Exception as e:
            return email
        raise forms.ValidationError(f"Email {email} is already in use.")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = False
        if commit:
            user.save()
        return user

class ReactivateEmailForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = EmailActivation.objects.email_exists(email)
        if not qs.exists():
            register_link = reverse("accounts:register")
            msg = """This email does not exists, would you like to <a href="{link}">register</a>?
            """.format(link=register_link)
            raise forms.ValidationError(mark_safe(msg))
        return email
