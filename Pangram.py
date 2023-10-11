import string

def is_pangram(s):
    s = s.lower()
    alphabet = set(string.ascii_lowercase)
    return set(s) >= alphabet

# Example usage:
sentence = input("Enter a sentence: ")
if is_pangram(sentence):
    print("The input is a pangram.")
else:
    print("The input is not a pangram.")