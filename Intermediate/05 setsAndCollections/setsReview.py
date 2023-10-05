music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Write your code below!
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

# Get union of the 2 sets, returning a frozenset
frozen_tag_union = my_tags | music_tags
print(frozen_tag_union)

# Get intersection of the 2 sets, normal set
regular_tag_intersect = music_tags & my_tags
print(regular_tag_intersect)

# Get difference of the 2, returning frozenset
frozen_tag_difference = my_tags - music_tags
print(frozen_tag_difference)

# Get symmetric difference, returning normal
regular_tag_sd = music_tags ^ my_tags
print(regular_tag_sd)