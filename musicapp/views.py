from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import (
    PostArtisteSerializer,
    GetArtisteSerializer,
    PostSongSerializer,
    GetSongSerializer,
    UpdateSongSerializer
    #PostLyricsSerializer,
    #GetLyricsSerializer
)
from .models import Artiste, Song #Lyrics


# Create your views here.

class ArtisteAPIView(APIView):
  
   def get(self, request):
        artistes = Artiste.objects.all()
        serializer = GetArtisteSerializer(artistes, many=True)
        return Response(serializer.data) 


   def post(self, request):
        serializer = PostArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongAPIView(APIView):
  
   def get(self, request):
        songs = Song.objects.all()
        serializer = GetSongSerializer(songs, many=True)
        return Response(serializer.data) 


   def post(self, request):
        serializer = PostSongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""class LyricsAPIView(APIView):
  
   def get(self, request):
        lyrics = Lyrics.objects.all()
        serializer = GetLyricsSerializer(lyrics, many=True)
        return Response(serializer.data) 


   def post(self, request):
        serializer = PostLyricsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

class SongDetailsAPIView(APIView):
    def song_details(self, id):

        try:
            return Song.objects.get(id=id)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        song = self.song_details(id)
        serializer = GetSongSerializer(song)
        return Response(serializer.data)

    def put(self, request, id):
        song = self.song_details(id)
        serializer = UpdateSongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = self.song_details(id)
        song.delete()
        return Response(status=status.HTTP_200_OK)
    


