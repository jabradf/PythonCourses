song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'], 
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Write your code below!
# either .union, or | as operators
# the left side is the inherited type (eg frozenset)

new_song_data = {}
for key,val in song_data.items():
  #print(song_data)
  songD = set(song_data[key])
  tagD = set(user_tag_data[key])
  new_song_data[key] = songD.union(tagD)

print(new_song_data)