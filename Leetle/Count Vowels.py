def solve(text):
  lowercase_text = text.lower()
  vowels = set(["a","e","i","o","u"])
  cnt = 0
  for char in lowercase_text:
    if char in vowels:
      cnt+=1
  return cnt

    # List Comprehension
def solve(text):
  return sum(1 for c in text.lower() if c in 'aeiou')
