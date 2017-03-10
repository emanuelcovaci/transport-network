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
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from .forms import SendMailForm
from django.core.mail import send_mail


def contact(request):

    if request.method == "POST":
        send_form = SendMailForm(request.POST)
        confirm = []
        if send_form.is_valid():
            subject = "Comanda"
            messages = send_form.cleaned_data['sender_text']
            from_email = settings.EMAIL_HOST_USER
            to_list = [send_form.cleaned_data['sender_email'],settings.EMAIL_HOST_USER]
            send_mail(subject,messages,from_email,to_list,fail_silently=True)
            confirm.append("Mesajul a fost trimis!")
            return render(request, 'contact/contact.html', context={'form': send_form,
                                                                    'messages': confirm})
        else:
            return render(request, 'contact/contact.html', context={'form': send_form})
    else:
        send_form = SendMailForm()
        return render(request, 'contact/contact.html', context={'form': send_form})
