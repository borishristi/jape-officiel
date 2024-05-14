from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=50, required=False, strip=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField( required=True, widget=forms.Textarea())
    cgu_accept = forms.BooleanField(initial=True)
