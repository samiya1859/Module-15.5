from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.


def add_album(request):
    if request.method=='POST':
        album_form = forms.AlbumModelForm()
        if album_form.is_valid():
            album_form.save()
            return redirect('album')
    else:
        album_form=forms.AlbumModelForm()
    return render(request,'album.html',{'form':album_form})

def edit_album(request,id):
    album = models.AlbumModel.objects.get(pk=id)
    album_form = forms.AlbumModelForm(instance=album)
    if request.method=='POST':
        album_form = forms.AlbumModelForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request,'album.html',{'form':album_form})

def delete_post(request,id):
    album = models.AlbumModel.objects.get(pk=id)
    album.delete()
    return redirect('home')
    
