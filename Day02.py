input_value = open("D:\Practice\work\Python\Projects\AdventOfCode2023\Inputs\Day02.txt", "r").readlines()
running_total = 0
maxBlue = 12
maxRed = 13
maxGreen = 14
Game = 0
current = []
pull = []
ValidGame = True
def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

for current_game in input_value:
    current = current_game.split(": ")[1]
    current = current.split("; ")
    Game += 1
    for pull in current: #separate individual pulls
        pull = pull.split(", ")
        for color in pull:
            if "blue" in color and ValidGame == True:
                if get_num(color) > maxBlue:
                    print(f"Too many Blue Dice in {pull}! Current Game: {Game}")
                    ValidGame = False
            if "green" in color and ValidGame == True:
                if get_num(color) > maxGreen:
                    print(f"Too many Green Dice in {pull}! Current Game: {Game}")
                    ValidGame = False
            if "red" in color and ValidGame == True:
                if get_num(color) > maxRed:
                    print(f"Too many Red Dice in {pull}! Current Game: {Game}")
                    ValidGame = False
    if ValidGame == True:
        running_total += Game
    ValidGame = True
print(f"Current Game: {Game}. Running total: {running_total}")
