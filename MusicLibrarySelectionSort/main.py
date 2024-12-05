from music_library import MusicLibrary
from song import Song 
def main():
  library = MusicLibrary()
  
  # Load songs from the file
  library.load_songs_from_file('songs.json')
  print("All songs in the library:")
  library.display_all_songs()

  library.top_songs_by_score()
  library.top_songs_by_danceability()
  
  print("\nSongs sorted by Score:")
  library.selection_sort_by_score()
  library.display_all_songs()
  
  print("\nSongs sorted by Danceability:")
  library.selection_sort_by_danceability()
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

  print("------------------------------------------------")
  test_selection_sort(MusicLibrary())  

def test_selection_sort(library):
    new_library = MusicLibrary()
    new_library.add_song(Song("Song 1", "Artist 1", score=3))
    new_library.add_song(Song("Song 2", "Artist 2", score=3))
    new_library.add_song(Song("Song 3", "Artist 3", score=7))
    new_library.add_song(Song("Song 4", "Artist 4", score=100))

    new_library.selection_sort_by_score()

    new_library.display_all_songs()


if __name__ == "__main__":
    main()