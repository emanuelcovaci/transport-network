from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from .forms import SendMailForm
from django.core.mail import send_mail


def contact(request):

    if request.method == "POST":
        send_form = SendMailForm(request.POST)
        if send_form.is_valid():
            send_mail("Comanda Transport", send_form.cleaned_data['sender_text'], send_form.cleaned_data['sender_email'],
                      [settings.EMAIL_HOST_USER], fail_silently=True)
            messages.success(request, "Comanda ta a fost transmisa cu success")
            return render(request, 'contact/contact.html', context={'form': send_form})
        else:
            return render(request, 'contact/contact.html', context={'form': send_form})
    else:
        send_form = SendMailForm()
        return render(request, 'contact/contact.html', context={'form': send_form})
