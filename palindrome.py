from string import punctuation as allpunctuations

def is_palindrome(string):
    for punctuation in allpunctuations:
        if punctuation in string[0:]:
            string = string.replace(punctuation, "")
    if string == string[::-1]:
        return True
    else:
        return False


while True:
    print(is_palindrome(input("String: ").lower().strip()))