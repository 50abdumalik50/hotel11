from django import forms

from apps.pages.models import Service, Team, Facilities, Contact, About


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'name',
            'description',
        ]


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'name',
            'occupation',
            'image_for_team',

        ]


class FacilitiesForm(forms.ModelForm):
    class Meta:
        model = Facilities
        fields = [
            'name',
            'description',
            ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'number',
            'email',
            'subject',
            # 'message',
        ]


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = [
            'title',
            'description',
        ]