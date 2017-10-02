from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import (

authenticate,
get_user_model,
login,
logout
)

User    = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='user name',max_length=30, required=False, help_text='')
    email = forms.EmailField(max_length=50, help_text='')
    password1 = forms.CharField(label='password',widget=forms.PasswordInput,max_length=30, required=True, help_text='')
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput,max_length=30, required=True, help_text='')



    class Meta:
        model = User
        fields = ('username','email','password1', 'password2', )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')


    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")

        if sum(c.isdigit() for c in password2) < 2:
            raise forms.ValidationError('Password must container at least 2 digits.')
        if not any(c.isupper() for c in password2):
            raise forms.ValidationError('Password must container at least 1 uppercas')

        return password2


class GetMessageForm(forms.Form):
    reciever        = forms.SelectMultiple()
    message_content = forms.CharField()






























