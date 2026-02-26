# Python code below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def count_numbers(which, numbers):
    # Your code goes here
    count = 0
    if which == "even":
        for i in range (0,len(numbers)):
            if numbers[i] == which or numbers[i] % 2 == 0:
                count += 1
        return count
    elif which == "odd":
        for i in range(0, len(numbers)):
            if numbers[i] == which or numbers[i] % 2 != 0:
                count += 1
        return count
    return -1

numbers = [7, 17, 2, 13, 19, 20, 0, 5, 11, 1280, 105]

result1 = count_numbers("even", numbers)
result2 = count_numbers("odd", numbers)
result3 = count_numbers("Blarg", numbers)
print(result1, result2, result3)
