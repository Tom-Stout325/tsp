from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=100, label = "Name")
    contact_email = forms.EmailField(label = "Email")
    message = forms.CharField(widget=forms.Textarea, label = "Message")

 