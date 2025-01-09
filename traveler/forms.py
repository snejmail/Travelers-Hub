from django import forms

from .models import Traveler


class CreateTravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ('nickname', 'email', 'country',)

        help_texts = {
            'nickname': "*Nicknames can contain only letters and digits.",
        }

        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': "Enter a unique nickname...",
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': "Enter a valid email address...",
            }),
            'country': forms.TextInput(attrs={
                'placeholder': "Enter a country code like <BGR>...",
            })
        }
        labels = {
            'nickname': "Nickname:",
            'email': "Email:",
            'country': "Country:",
        }


class EditTravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ('nickname', 'email', 'country', 'about_me')

        help_texts = {
            'nickname': "*Nicknames can contain only letters and digits.",
        }

        labels = {
            'nickname': "Nickname:",
            'email': "Email:",
            'country': "Country:",
            'about_me': "About me:",
        }


class DeleteTravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ()
        