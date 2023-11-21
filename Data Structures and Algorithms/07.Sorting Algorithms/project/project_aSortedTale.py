import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

#for book in bookshelf:
#  print(book)

#print(ord("a"))
#print(ord(" "))
#print(ord("A"))

def by_title_ascending(book_a, book_b):
  if book_a['title_lower'] > book_b['title_lower']:
    return True
  else:
    return False

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

# checkpoint 7:
#for book in sort_1:
#  print(book['title'])
  # there were 2 swaps

def by_author_ascending(book_a, book_b):
  if book_a['author_lower'] > book_b['author_lower']:
    return True
  else:
    return False

# checkpoint 9
#bookshelf_v1 = bookshelf.copy()
#sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

# checkpoint 10
#for book in sort_2:
#  print(book['author'])
  # there were 26 swaps

# checkpoint 14
#bookshelf_v2 = bookshelf.copy()
#sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)

# checkpoint 15
#for book in bookshelf_v2:
  #print(book['author'])
  # there were 26 swaps

# checkpoint 16
def by_total_length(book_a, book_b):
  len1 = len(book_a['author_lower'] + book_a['title_lower'])
  len2 = len(book_b['author_lower'] + book_b['title_lower'])

  if len1 > len2:
    return True
  else:
    return False

# checkpoint 17
long_bookshelf = utils.load_books('books_large.csv')
# checkpoint 18
#sort_2 = sorts.bubble_sort(long_bookshelf, by_total_length) # 1082069 swaps done, slow!
sort_3 = sorts.quicksort(long_bookshelf, 0, len(long_bookshelf)-1, by_total_length) # finishes a lot quicker!