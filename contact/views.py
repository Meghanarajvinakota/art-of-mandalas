from django.shortcuts import render
from django.contrib import messages
from .models import ContactForm
from .forms import ContactUsForm

# Create your views here.


def contact_us(request):
    """
    Renders the contcat form on the contact page
    for the website :model:`contact/conatct.html`.
    """

    if request.method == "POST":
        contact_us_form = ContactUsForm(data=request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 ("Thanks for your message! "
                                  "I will try to read and respond "
                                  "within 5 working days."))
    """
    Renders the Contact page
    """
    contact_us_form = ContactUsForm

    return render(
        request,
        "contact/contact.html",
        {"contact_us_form": contact_us_form},
    )
