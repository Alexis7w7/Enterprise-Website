from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage


# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            mail = request.POST.get('mail', '')
            content = request.POST.get('content', '')

            # creating the email
            mail = EmailMessage(
                "La sabrosa: new message contact",  # asunto
                "from {}{}\n\nTyped:\n\n{}".format(name, mail, content),  # message
                "lasabrosa.com",  # email address
                ["yourEmail@xx.com"],  # destination
                reply_to=[mail]
            )

            # sending and redirecting
            try:
                mail.send()
                # everything is ok
                return redirect(reverse('contact')+'?ok')
            except:
                # something went wrong
                return redirect(reverse('contact')+'?fail')
    return render(request, 'contact/contact.html', {'form': contact_form})
