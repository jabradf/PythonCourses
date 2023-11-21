# Naive Pattern Search
Test your understanding of naive pattern search with code challenges!

## Review of Naive Pattern Search
Naive pattern search is a simple way to systemically look through a text for a given pattern. This algorithm iterates over each character in a text and then counts the following number of matching characters to find the pattern. It is preferred for its simplicity and ease of implementation, allowing it to easily be modified for other purposes.

## Summary of Tasks
Our friend has asked us to review and edit the introduction to their paper. Luckily the mistakes are all generally similar, such as misspellings of the same word and a repeated glitch from a software bug. This will require us to extend our naive pattern search algorithm functionality to not just find patterns, but replace them as well! This will be done through the following steps:

1. Find patterns more easily by making the search case-insensitive.
2. Build and maintain a separate copy of the introduction to insert replacements.
3. Skip newly-replaced characters.

## Find Patterns with Case Insensitivity
A good starting point to enhance our naive pattern search algorithm and help our friend is to add case insensitivity. This will allow the code to find matching words regardless of the capitalization, thereby letting us more easily fix a misspelled word no matter if it is at the beginning or the middle of a sentence. For example, searching for "hello" would match `"Hello"`, `"heLLo"`, and every other possible combination of capitalized letters. This is needed as our friend’s paper has some very sporadic capitalization as well as typos in both the uppercase and lowercase versions of "pylhon".

```
def pattern_search(text, pattern, case_sensitive=True):
  for index in range(len(text)):
    match_count = 0
    for char in range(len(pattern)): 
      if (pattern[char] == text[index + char]) or (not case_sensitive and pattern[char] == text[index + char].lower()):
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language")
pattern_search(friends_intro, "pylhon", False)
pattern_search(friends_intro, "idil", False)
```

Let’s step through the completed code. Most of these modifications to `pattern_search` are checks on your knowledge of Python syntax and language features. Optional parameters are added like usual with an additional equals to assign their default value.

Checking for case sensitivity revolves around utilizing this new parameter and the String `lower()` method. The `case_sensitive` parameter can either be validated in an additional layer of conditional statements or compacted into the existing logic with the use of the `and` keyword.

## Replace Found Words
Now to the meat of the issue, replacing words in our friend’s introduction. This will be very helpful as some sort of bug has littered the same ``zzz`` pattern throughout their introduction, but this also adds the most complexity to the algorithm.

As the algorithm iterates through the given text, it cannot be directly modified without breaking the `for` loop and causing string indexing errors. A new variable will be needed to append characters without any matches, as to maintain the original sections of the text, as well as the `replacement` patterns. Similarly, our `replacement` pattern may not be of equal length to the found `pattern`. Iterations of the search algorithm must therefore be skipped as to not overwrite the newly inserted `replacement` characters.

The additional modifications required to add a replacement feature to the `pattern_search` function can be split into two sections:

### Maintaining the Fixed Text
1. Add an additional `replacement` input parameter to the function definition for the text that will replace the found `pattern`.
2. Initialize a `fixed_text` variable at the top of the function that will serve as a placeholder for the completed text containing all the necessary replacements to be returned at the end of the function
3. When the `pattern` is found, the `replacement` should now be appended to the `fixed_text`. In all other cases, append the currently iterating `text` character to the `fixed_text` to ensure that the rest of the original text is being maintained.


### Skipping Replaced Characters
1. Initialize a `num_skips` variable set to `0` right after the initialization of the `fixed_text` variable. This will track the numbers of characters that need to be skipped during the search, as a `pattern` was already found, and the relevant characters in the text already replaced.
2. While iterating through the `text` indices, if `num_skips` is greater than `0`, decrement it by `1` and continue to the next iteration of the `for` loop. This logic allows for the actual skipping of the replaced characters.
3. Right after the `replacement` is appended to the `fixed_text`, set `num_skips` to the length of the pattern minus `1`. This sets the number of following search iterations to skip. `1` must be subtracted to account for the current iteration.

```
def pattern_search(text, pattern, replacement, case_sensitive=True):
  fixed_text = ""
  num_skips = 0

  for index in range(len(text)):
    if num_skips > 0:
      num_skips -= 1
      continue
    
    match_count = 0

    for char in range(len(pattern)): 
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break

    if match_count == len(pattern):
      print(pattern, "found at index", index)
      fixed_text += replacement
      num_skips = len(pattern)-1
    else:
      fixed_text += text[index]

  return fixed_text

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language", "language")
pattern_search(friends_intro, "pylhon", "Python", False)
pattern_search(friends_intro, "idil", "ideal", False)
pattern_search(friends_intro, "zzz ", "")
pattern_search(friends_intro, "syntacs", "syntax")
pattern_search(friends_intro, "languuUuage", "language")
```

Now to walkthrough the completed code. The first step is to create a `fixed_text` placeholder that will act as a safe copy of the original `text` and build this duplicate out character-by-character. This is needed to prevent out-of-bounds errors related to changing the length of the `text` being iterated. Adding in replacement patterns means that the following characters from the original `text` should no longer be copied over, as to not overwrite the replacement. Luckily, as the `pattern` is the item being replaced, we can use its length to determine the amount of search iterations to skip using the continue keyword. `1` must be subtracted from this length to account for the replacement of the current character.

# Reviewing Replacements with Naive Pattern Search
You made it!

In this code challenge you took your understanding of naive pattern search and expanded it by adding case insensitivity and a method for replacing found patterns.

Hopefully these exercises show the trove of possibilities for expanding the algorithm for other uses. For example, what if the matching criteria was different? Could a `pattern` still be found if there was a typo in the `text`? What about if instead of comparing single characters, each word was compared?

With such a malleable algorithm the potential is just waiting to be unlocked!