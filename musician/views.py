from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_musician(request):
    if request.method=='POST':
        musician_form = forms.MusicianModelForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    else:
        musician_form=forms.MusicianModelForm()
    return render(request,'music.html',{'form':musician_form})

def edit_musician(request,id):
    musician = models.MusicianModel.objects.get(pk=id)
    musician_form = forms.MusicianModelForm(instance=musician)
    if request.method=='POST':
        musician_form = forms.MusicianModelForm(request.POST,instance=musician)
        if musician_form.is_valid():
           musician_form.save()
           return redirect('home')
    return render(request,'music.html',{'form':musician_form})