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
    form = NoteForm()
    return render(request, 'core/notes_edit.html', {'form': form})