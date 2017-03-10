# Copyright 2017-2020 Emanuel Covaci, Rares Istoc
#
# This file is part of Transport Network.
#
# Transport Network is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Transport Network is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Transport Network.  If not, see <http://www.gnu.org/licenses/>.
from django import forms
from django.core.validators import validate_email
from captcha.fields import ReCaptchaField


class SendMailForm(forms.Form):
    re_captcha = ReCaptchaField(
        attrs={'lang': 'ro'}
    )
    sender_name = forms.CharField(label="Name", widget=forms.TextInput(attrs={}), required=True)
    sender_email = forms.CharField(label="Email", widget=forms.EmailInput(attrs={}), required=True)
    sender_text = forms.CharField(widget=forms.Textarea(), required=True)

    def __init__(self, *args, **kwargs):
        super(SendMailForm, self).__init__(*args, **kwargs)

    def clean_sender_email(self):
        email = self.cleaned_data.get('sender_email')
        if validate_email(email):
            raise forms.ValidationError("Introduceti un email valid!")
        return email
