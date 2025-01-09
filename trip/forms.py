from django import forms

from trip.models import Trip


class BaseClassTripForm(forms.ModelForm):
    class Meta:
        model = Trip
        exclude = ('traveler',)


class CreateTripForm(BaseClassTripForm):
    class Meta:
        model = Trip
        exclude = ('traveler',)

        help_texts = {
            'duration': "*Duration in days is expected.",
        }

        labels = {
            'destination': 'Destination:',
            'summary': 'Summary:',
            'start_date': 'Started on:',
            'duration': 'Duration:',
            'image_url': 'Image URL:',
        }

        widgets = {
            'destination': forms.TextInput(attrs={
                'placeholder': "Enter a short destination note...",
            }),
            'summary': forms.Textarea(attrs={
                'placeholder': "Share your exciting moments... ",
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': "An optional image URL...",
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['duration'].initial = 1


class EditTripForm(BaseClassTripForm):
    pass


class DeleteTripForm(BaseClassTripForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'



