from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'last_qualification',
            'percentage_year',
            'location',
            'course_interest',
            'english_test'
        ]
