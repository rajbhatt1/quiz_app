from django import forms 
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','fullname','role', 'password1', 'password2',]

class admin_SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','fullname', 'password1', 'password2',]

class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data["email"]
        query = User.objects.filter(email=email)

        if not query.exists():
            raise forms.ValidationError("Email not exists!!!")
        elif not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email domain not valid!!!")
        return email
        
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Credential not match!!!")
        return cleaned_data
