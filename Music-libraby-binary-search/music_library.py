import json
from song import Song


class MusicLibrary:

  def __init__(self):
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    self.songs.sort()

  def load_songs_from_file(self, file_path):
    with open(file_path, 'r') as file:
      data = json.load(file)
      for item in data['songs']:
        song = Song(
          title=item['title'],
          artist=item['artist'],
          score=item.get('score', 0),
          genre=item.get('genre', ""),
          danceability=item.get('danceability', 0.0),
          energy=item.get('energy', 0.0),
          valence=item.get('valence', 0.0),
          duration=item.get('duration', 0),
          )
        self.add_song(song)

  def display_all_songs(self):
    headers = f"{'Title':25} {'Artist':20} {'Score':5} {'Genre':10} {'Danceability':12} {'Energy':10} {'Valence':10} {'Duration':8}"
    print(headers)
    print('-' * len(headers))
    for song in self.songs:
      print(song)

  def sort_by_title(self):
    self.songs.sort(key=lambda x: x.title)

  def binary_search(self, title):
    low, high = 0, len(self.songs) - 1
    while low <= high:
      mid = (low + high) // 2
      if self.songs[mid].title == title:
        return self.songs[mid]
      elif self.songs[mid].title < title:
        low = mid + 1
      else:
        high = mid - 1
    return None

  def display_songs(self, songs):
    headers = f"{'Title':25} {'Artist':20} {'Score':5} {'Genre':10} {'Danceability':12} {'Energy':10} {'Valence':10} {'Duration':8}"
    print(headers)
    print('-' * len(headers))
    for song in songs:
      print(song)