input_value = open("D:\Practice\work\Python\Projects\AdventOfCode2023\Inputs\Day03Example.txt", "r").readlines()
SymbolPositionCurrent = []
SymbolPositionLast = []
SymbolPositionNext = []
DigitPosition = []
Current = 0
ValidDigits = []
running_total = 0
Numbers = ""

for CurrentLine in input_value:
    SymbolPositionLast = SymbolPositionCurrent
    SymbolPositionCurrent = SymbolPositionNext
    SymbolPositionNext = []
    DigitPosition = []
    for index,char in enumerate(CurrentLine):
        #find all digits and log index
        if char.isdigit() and index in SymbolPositionLast:
            DigitPosition.append(index)
            Numbers.join(char)
        # find all symbols that aren't "." or linebreak
        elif "." not in char:
            if "\n" not in char:
                SymbolPositionCurrent.append(index - 1)
                SymbolPositionCurrent.append(index)
                SymbolPositionCurrent.append(index + 1)
    print(f"{Current} Previous line: {SymbolPositionLast}")
    Current += 1
    print(f"{Current} Current line: {SymbolPositionCurrent}")
    print(f"Found valid digits at {DigitPosition} in line {Current}")