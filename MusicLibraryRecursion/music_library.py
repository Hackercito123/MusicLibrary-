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

  def selection_sort_by_score(self):
    for i in range(len(self.songs)):
      max_idx = i
      for j in range(i + 1, len(self.songs)):
        if self.songs[j].score > self.songs[max_idx].score:
          max_idx = j
      self.songs[i], self.songs[max_idx] = self.songs[max_idx], self.songs[i]

  def selection_sort_by_danceability(self):
    for i in range(len(self.songs)):
      max_idx = i
      for j in range(i + 1, len(self.songs)):
        if self.songs[j].danceability > self.songs[max_idx].danceability:
          max_idx = j
      self.songs[i], self.songs[max_idx] = self.songs[max_idx], self.songs[i]
      
  def top_songs_by_score(self, n=10):
      self.selection_sort_by_score()
      print("\nTop Songs by Score:")
      self.display_songs(self.songs[:n])
    
  def top_songs_by_danceability(self, n=10):
      self.selection_sort_by_danceability()
      print("\nTop Songs by Danceability:")
      self.display_songs(self.songs[:n])

  
  def display_songs(self, songs):
    headers = f"{'Title':25} {'Artist':20} {'Score':5} {'Genre':10} {'Danceability':12} {'Energy':10} {'Valence':10} {'Duration':8}"
    print(headers)
    print('-' * len(headers))
    for song in songs:
      print(song)

  def recursive_display(self, index=0):
    if index == 0:
      headers = f"{'Title':25} {'Artist':20} {'Score':5} {'Genre':10} {'Danceability':12} {'Energy':10} {'Valence':10} {'Duration':8}"
      print(headers)
      print('-' * len(headers))
    if index == len(self.songs):
      return
    print(self.songs[index])
    self.recursive_display(index + 1)

  def recursive_search(self, title, low=0, high=None):
    if high is None:
      high = len(self.songs) - 1
    if low > high:
      return None
    mid = (low + high) // 2
    if self.songs[mid].title == title:
      return self.songs[mid]
    elif self.songs[mid].title < title:
      return self.recursive_search(title, mid + 1, high)
    else:
      return self.recursive_search(title, low, mid - 1)