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
                    ValidGame = False
            if "green" in color and ValidGame == True:
                if get_num(color) > maxGreen:
                    ValidGame = False
            if "red" in color and ValidGame == True:
                if get_num(color) > maxRed:
                    ValidGame = False
    if ValidGame == True:
        running_total += Game
    print(f"Current Game: {Game}. Running total: {running_total}")
    ValidGame = True