from django.shortcuts import render, redirect

from notes.web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm, DetailsNoteForm
from notes.web.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    notes = Note.objects.all()
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateNoteForm()
    context = {
        'form': form,
        'no_note': True,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteNoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DetailsNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DetailsNoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-details.html', context)


def show_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    context = {
        'profile': profile,
        'notes': len(notes),
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    Note.objects.all().delete()
    profile.delete()
    return redirect('show index')
