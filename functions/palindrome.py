
def is_palindrome(text):

    if text == text[::-1]:
        return True
    else:
        return False


# Taking input
word = input("Enter a word: ").lower()

if is_palindrome(word):
    print(word, "is a Palindrome")
else:
    print(word, "is not a Palindrome")
