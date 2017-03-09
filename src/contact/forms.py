from django import forms


class SendMailForm(forms.Form):

    sender_name = forms.CharField(label="Name", widget=forms.TextInput(attrs={}), required=True)
    sender_email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={}), required=True)
    sender_text = forms.CharField(widget=forms.Textarea(), required=True)

    def __init__(self, *args, **kwargs):
        super(SendMailForm, self).__init__(*args, **kwargs)

    def clean_sender_email(self):
        email = self.cleaned_data.get('sender_email')

        if '@' in email:
            return email
        else:
            forms.ValidationError("Introduce un email valid. Verifica daca ai scris adresa corect , "
                                  "trebuie sa contina caracterul @ si domeniul.com ex: nume_utilizator@gmail.com")
