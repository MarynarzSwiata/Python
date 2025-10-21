favorite_songs = ["Car Music 2024", "DubStep Hits 2025", "Lofi Chill Vibes 2025"]
user_song = input("Enter your favorite song: ")

if user_song in favorite_songs:
    print(f"{user_song} is in the playlist.")
else:
    print(f"{user_song} is not in the playlist.")
    print("These are the current songs in the playlist:\n")
    for index, song in enumerate(favorite_songs, start=1):
        print(f"{index}. {song}")


print(f"My favorite songs are: {favorite_songs[0]} and {favorite_songs[2]}")
favorite_songs.append("Classical Essentials 2023")
print(f"Updated playlist: {favorite_songs}, total songs: {len(favorite_songs)}")
favorite_songs.pop()
print(
    f"After removing the last song: {favorite_songs}, total songs: {len(favorite_songs)}"
)
