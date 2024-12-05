from music_library import MusicLibrary
from song import Song 
def main():
  library = MusicLibrary()
  
  # Load songs from the file
  library.load_songs_from_file('songs.json')
  print("All songs in the library:")
  library.display_all_songs()

  
  
      # Binary search demonstration (from previous lab)
  library.sort_by_title()
  print("\nBinary Search Demonstration:")
  search_title = "Go Crazy"
  result = library.binary_search(search_title)
  if result:
    print(f"Found: {result}")
  else:
    print(f"\n'{search_title}' not found.")
    
    search_title = "Imaginary Song"
    result = library.binary_search(search_title)
  if result:
    print(f"\nFound: {result}")
  else:
    print(f"\n'{search_title}' not found.")

  print("--------------------------------------------------------------------")

  # Test QuickSort by Duration
  library.display_songs_sorted_by_duration()

  test_quick_sort()

def test_quick_sort():

    Library_1 = MusicLibrary()
    Library_1.add_song(Song("Song 3", "Artist", duration=160))
    Library_1.add_song(Song("Song 2", "Artist", duration=160))
    Library_1.add_song(Song("Song 5", "Artist", duration=160))
    Library_1.add_song(Song("Song 1", "Artist", duration=160))
    Library_1.add_song(Song("Song 4", "Artist", duration=160))
    Library_1.display_songs_sorted_by_duration()

    Library_2 = MusicLibrary()
    Library_2.add_song(Song("Song 3", "Artist", duration=160))
    Library_2.add_song(Song("Song 2", "Artist", duration=161))
    Library_2.add_song(Song("Song 5", "Artist", duration=162))
    Library_2.add_song(Song("Song 1", "Artist", duration=163))
    Library_2.add_song(Song("Song 4", "Artist", duration=164))
    Library_2.display_songs_sorted_by_duration()

    Library_3 = MusicLibrary()
    Library_3.add_song(Song("Song 3", "Artist", duration=164))
    Library_3.add_song(Song("Song 2", "Artist", duration=163))
    Library_3.add_song(Song("Song 5", "Artist", duration=162))
    Library_3.add_song(Song("Song 1", "Artist", duration=161))
    Library_3.add_song(Song("Song 4", "Artist", duration=160))
    Library_3.display_songs_sorted_by_duration()

    Library_4 = MusicLibrary()
    Library_4.add_song(Song("Song 3", "Artist", duration=1))
    Library_4.add_song(Song("Song 2", "Artist", duration=116))
    Library_4.add_song(Song("Song 5", "Artist", duration=17000))
    Library_4.add_song(Song("Song 1", "Artist", duration=60))
    Library_4.add_song(Song("Song 4", "Artist", duration=160))
    Library_4.display_songs_sorted_by_duration()



if __name__ == "__main__":
    main() 