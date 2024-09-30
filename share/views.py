from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Share
from .forms import ShareAnArtForm

# Create your views here.

"""
Form for users to share an Art
"""
def share_an_art(request):
    shared_list = Share.objects.all().filter(
        approved = True)
    if request.method == "POST":
        share_an_art_form = ShareAnArtForm(request.POST, request.FILES)
        if share_an_art_form.is_valid():
            shared_art = share_an_art_form.save(commit = False)
            shared_art.name = request.user.username
            shared_art.save()
            messages.add_message(request, messages.SUCCESS, "Thanks for sharing!!")

    """
    Renders the Share page
    """

    share_an_art_form = ShareAnArtForm
    return render(
        request,
        "share/share.html",
        {"share_an_art_form": share_an_art_form,
        'shared':shared_list}
 )

"""
    Edit a shared post
    """
def share_edit(request, share_id):
 
    if request.method == "POST":
        share_to_edit = get_object_or_404(Share, pk=share_id)
        share_an_art_form = ShareAnArtForm(request.POST, request.FILES)
        if share_an_art_form.is_valid():
            share_to_edit.author = request.POST.get('author')
            share_to_edit.title = request.POST.get('title')
            share_to_edit.save()
            messages.add_message(request, messages.SUCCESS, "Updated !!")
        else:
            messages.add_message(request, messages.ERROR,
            'Error updating art!')
        return redirect('share')

def share_delete(request, share_id):
    """
    Delete a shared post
    """
    share = get_object_or_404(Share, pk = share_id)
    if share.name == request.user.username:
        share.delete()
        messages.add_message(request, messages.SUCCESS, 'MandalaArt deleted!')
    else:
        messages.add_message(request, messages.ERROR,
            'You can only delete your own shared Mnadala art!')
    return redirect('share')