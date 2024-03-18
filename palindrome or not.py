def palindrome(s):
    for i in range(0, len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

string = input("Enter string: ")

if palindrome(string):
    print("The given string is palindrome.")
else:
    print("Not a palindrome.")
