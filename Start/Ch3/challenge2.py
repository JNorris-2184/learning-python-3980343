# Python code​​​​​​‌‌‌‌​​‌‌‌‌​​‌‌​​​‌​‌​‌‌​​ below
# Use print("messages...") to debug your solution.
import string
import re

show_expected_result = False
show_hints = False

def is_palindrome(teststr):
    # Your code goes here.
    if not teststr.isalnum():
        teststr = teststr.lower()
        pattern = r"[\s" + re.escape(string.punctuation) + r"]+"
        teststr = re.sub(pattern, '', teststr)
        right = -1
        for left in (range(0,int(len(teststr)/2))):
            if teststr[left] == teststr[right]:
                right -=1
                palindrome = True
            else:
                palindrome = False
                break
    return palindrome

#test_word = "Madam, I'm Adam."
# try using some of these other words:
#test_word = "RACE CAR!"
test_word = "Hello, world"
# test_word = "Radar?"
# test_word = "A man, a plan, a canal Panama!"

print(is_palindrome(test_word))