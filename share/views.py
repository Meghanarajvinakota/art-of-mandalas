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
            messages.add_message(request, messages.SUCCESS, "Thanks for sharing!! waiting for approval.")

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
    # Get the share instance to edit
    share_to_edit = get_object_or_404(Share, pk=share_id)

    # Ensure only the owner can edit
    if share_to_edit.name != request.user.username:
        messages.add_message(request, messages.ERROR, 'You can only edit your own posts!')
        return redirect('share')  # Redirect back if unauthorized

    # Handle the form submission
    if request.method == "POST":
        share_an_art_form = ShareAnArtForm(request.POST, request.FILES, instance=share_to_edit)
        
        if share_an_art_form.is_valid():
            share_an_art_form.save()  # Save the changes
            messages.add_message(request, messages.SUCCESS, "Updated successfully!")
            return redirect('share')  # Redirect to the main share page after saving
        else:
            messages.add_message(request, messages.ERROR, 'Error updating art!')
    
    else:
        # Prepopulate the form with the existing instance for GET requests
        share_an_art_form = ShareAnArtForm(instance=share_to_edit)

    return render(request, 'share/share_edit.html', {
        'form': share_an_art_form,
        'share': share_to_edit
    })

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