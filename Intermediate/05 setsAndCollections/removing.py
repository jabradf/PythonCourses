song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
# .remove() = removes an element, throws a key error if not found

# .discard() = removes an element, no error if not found

# neither works on frozen sets!
tag_set = set(song_data_users['Retro Words'])
tag_set.remove('onion')
tag_set.remove('helloworld')
tag_set.remove('spam')

song_data_users['Retro Words'] = tag_set
print(song_data_users)