from music_library import MusicLibrary
def main():
  library = MusicLibrary()
  
  # Load songs from the file
  library.load_songs_from_file('songs.json')
  print("All songs in the library:")
  library.display_all_songs()

  # Test the binary search with an example title
  # must sort by title for binary search to work
  library.sort_by_title()
  print("\nBinary Search Demonstration:")
  search_title = "Go Crazy"
  result = library.binary_search(search_title)
  if result:
    print(f"Found: {result}")
  else:
    print(f"\n'{search_title}' not found.")
    
  # Test with a song that doesn't exist
  search_title = "Imaginary Song"
  result = library.binary_search(search_title)
  if result:
    print(f"\nFound: {result}")
  else:
    print(f"\n'{search_title}' not found.")
  # In the main function:
  test_binary_search(library)
  # Test with empty library
  empty_library = MusicLibrary()
  test_binary_search(empty_library)
def test_binary_search(library):
  test_cases = [
    "Shape of You", # Assuming this is at the beginning
    "WAP", # Assuming this is at the end
    "Levitating", # Assuming this is in the middle
    "AAAAA", # Doesn't exist, would be at the beginning
    "ZZZZZ", # Doesn't exist, would be at the end
    "Imaginary Song", # Doesn't exist
    "A Very Long Song Title That Probably Doesn't Exist In The Library"
  ]
  for title in test_cases:
    result = library.binary_search(title)
    if result:
      print(f"Found: {result}")
    else:
      print(f"'{title}' not found.")
    
    
if __name__ == "__main__":
    main()