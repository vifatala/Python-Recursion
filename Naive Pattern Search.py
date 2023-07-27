"""
This is a  Naive Pattern Search algorithm I developed in my Codecademy course!
With this you can:
    * Insert your source text (text)
    * The word or phrase you are looking for (pattern), 
    * The new word or phrase you want to replace with (replacement),
    * And decide if you want the search to be case sensitive or not (case_sensitive).

There are some examples below! Uncomment them.
"""

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
        fixed_text += text[index]
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)
      fixed_text += replacement
      num_skips += len(pattern)-1
  return fixed_text

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
print(pattern_search(friends_intro, "Language", "language"))
# print("")
# print(pattern_search(friends_intro, "pylhon", "Python", False))
# print("")
# pattern_search(friends_intro, "idil", "ideal", False)
# pattern_search(friends_intro, "zzz ", "")
# print("")
# pattern_search(friends_intro, "syntacs", "syntax")
# print("")
# pattern_search(friends_intro, "languuUuage", "language")