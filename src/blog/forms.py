from django import forms

from blog.models import ContactForm


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["name", "email", "subject", "message"]

        labels = {"name": "Nom",
                  "email": "Email",
                  "subject": "Sujet",
                  "message": "Message"
                  }


