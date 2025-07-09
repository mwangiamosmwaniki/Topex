from django.shortcuts import render, redirect
from .models import Album, Photo
from .forms import PhotoUploadForm
from django.contrib.auth.decorators import login_required

def gallery_home(request):
    albums = Album.objects.all()
    return render(request, 'gallery/gallery_home.html', {'albums': albums})

def album_detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    return render(request, 'gallery/album_detail.html', {'album': album})

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery_home')
    else:
        form = PhotoUploadForm()
    return render(request, 'gallery/upload_photo.html', {'form': form})
