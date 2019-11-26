# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpRequest
import datetime
from .models import notes
from django.shortcuts import render,redirect
from .form import NotesForm
def home(request):
    text = {'note' : notes.objects.all()}
    return render(request,"index.html",text)

def add_notes(request):
    note = notes(text=request.POST['text'])
    note.save()
    return redirect('/notes/')

def delete_notes(request,id):
    delete_notes = notes.objects.get(id=id)
    delete_notes.delete()
    return redirect('/notes/')

def edit(request,id):
    if (request.method == "GET"):
        note = notes.objects.get(id=id)
        return render(request,'edit_notes.html',{'note':note})
    elif(request.method == "POST"):
        # id = request.POST.get("id")
        note = notes.objects.get(id=id)
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('/notes/')