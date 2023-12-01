input_value = open("D:\Practice\work\Python\Projects\AdventOfCode2023\Inputs\Day01.txt", "r").readlines()
running_total = 0

NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for current_input in input_value:
    value = ''
    digits = ''
    #convert words into digits - leave the first and last character in place to avoid overlaps
    for num, digit in NUMBERS.items():
        current_input = current_input.replace(num, f"{num[0]}{digit}{num[-1]}")
    for index,char in enumerate(current_input):
        # filter all digits into a placeholder integer
        if char.isdigit():
            value += char
    #take the first and last digit on the placeholder
    digits += value[0]
    digits += value[-1]
    #add to the total
    running_total += int(digits)
    print(running_total)