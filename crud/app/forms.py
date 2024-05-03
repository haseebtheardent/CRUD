from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from app.models import RecordTable

class Record(forms.ModelForm):
    class Meta:
        model = RecordTable  
        fields = ['first_name', 'last_name', 'email', 'phone', 'membership']


    first_name = forms.CharField(
        label='First Name',
        error_messages={'required': 'Please Enter Your first Name'},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Please Enter first Name',
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        label='Last Name',
        error_messages={'required': 'Please Enter Your Last Name'},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Please Enter Last Name',
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        initial='xyz@gmail.com',
        error_messages={'required': 'Please Enter Your Email'},
        widget=forms.TextInput(attrs={
            'placeholder': 'xyz@gmail.com',
            'class': 'form-control'
        })
    )

    phone = forms.CharField(
        label='Phone No',
        initial='12345678921',
        error_messages={'required': 'Please Enter Your Phone No'},
        label_suffix='!', 
        widget=forms.TextInput(attrs={
            'placeholder': '+923075239903',
            'class': 'form-control'
        })
    )

    membership = forms.ChoiceField(
        label='Please Choose Membership',
        widget=forms.Select(attrs={'class': 'form-select'}),
        choices=RecordTable.MEMBERSHIP_CHOICES
    )
