
from django.http import Http404
from .models import Album
from django.shortcuts import render
def index(request):
   all_album=Album.objects.all()
   context={'all_album':all_album}
   return render(request, 'music/index.html', context)
def details(request,album_id):
    try:
        album=Album.objects.get(pk=album_id)
        data={'album':album}
    except Album.DoesNotExist:
        raise Http404("Album Does not exist")
    return render(request,'music/detail.html',data)
