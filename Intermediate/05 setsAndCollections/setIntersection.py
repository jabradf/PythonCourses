song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

# Write your code below!
# get commonality between 2 sets using .intersection() or the & operator
# .intersection_update() returns updated set of the result
tags_int = set(user_recent_songs['Retro Words']) & set(user_recent_songs['Lowkey Space'])

print(tags_int)

recommended_songs = {}
for key, val in song_data.items():
  for tag in val:
    if tag in tags_int:
      if key not in user_recent_songs:
        recommended_songs[key] = val

print(recommended_songs)
