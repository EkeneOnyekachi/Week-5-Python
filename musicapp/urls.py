from django.urls import path
from .views import ArtisteAPIView, SongAPIView, SongDetailsAPIView #LyricsAPIView




urlpatterns = [
   path('artiste/', ArtisteAPIView.as_view()),
   path('song/', SongAPIView.as_view()),
   path('song_detail/<int:id>', SongDetailsAPIView.as_view()),
   #path('lyrics/', LyricsAPIView.as_view()),

]