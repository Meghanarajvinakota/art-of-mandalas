from django.shortcuts import render
from .models import About

# Create your views here.

def about_me(request):
    """
    Renders the most recent informatio on th website author
    Displays the invidiual instance of :model:`about.About`
    **Context**
    ``about``
        The most recent instance of :model:`about.About`
    **Template**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )