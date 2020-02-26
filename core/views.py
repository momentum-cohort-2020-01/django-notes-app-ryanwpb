from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse


from .models import Note
from .forms import NoteForm



def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note, "pk":pk})

def notes_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('notes-list')
    else:
        form = NoteForm()
    return render(request, 'core/notes_edit.html', {'form': form})

def notes_edit(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('notes-detail', note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'core/notes_edit.html', {'form': form})
