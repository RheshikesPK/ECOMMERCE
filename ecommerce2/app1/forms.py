
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile,Review
from django.contrib.auth.forms import AuthenticationForm


class SignInForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20, required=False)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=UserProfile.GENDER_CHOICES, required=False)

class Meta(UserCreationForm.Meta):
    model = User
    fields = ('username', 'email', 'password1', 'password2', 'shipping_address', 'phone_number', 'age', 'gender')

class ReviewForm(forms.ModelForm):
    class Meta:
        model= Review
        fields = ['review',]

        widgets = {
            'review' : forms.Textarea(attrs={'class':'input'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'City'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'State'}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'ZIP Code'}))
    