from rest_framework import serializers
from .models import Artiste, Song #Lyrics


class PostArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['first_name', 'last_name', 'age']


class GetArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ['first_name', 'last_name']


class PostSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'date_released', 'likes', 'artiste_id']


class GetSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'date_released', 'likes']


class UpdateSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'date_released']
    

"""class GetLyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = ['content']

    
class PostLyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = ['content', 'song_id']"""
