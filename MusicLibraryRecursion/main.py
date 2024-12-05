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

  print("------------------------------------------------")
  test_recursion(library)  

def test_recursion(library):
  print(library.recursive_search("Astronaut In The Ocean"))
  print(library.recursive_search("WHATS NEXT"))
  print(library.recursive_search("Mood"))
  print(library.recursive_search("AAAAAAA"))
  print(library.recursive_search("ZZZZZZZ"))
  print(library.recursive_search("This is a very long title"))

  print("---------------------------------------------------------------")
  empty_library = MusicLibrary()
  print(empty_library.recursive_search("Astronaut In The Ocean"))

        
if __name__ == "__main__":
    main()