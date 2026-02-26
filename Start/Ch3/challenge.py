# Python code below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def find_longest(strings):
    # Your code goes here
    length = 0
    longest = 0
    for i in range(0,len(test_strings)):
        if len(test_strings[i]) > length:
            length = len(test_strings[i])
            longest = i
    return longest

test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]
print(longest_strings[find_longest(test_strings)])

