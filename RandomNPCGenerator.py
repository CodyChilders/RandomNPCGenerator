from random import randint as rand

diceSize = 6 #setting this to 8 makes it a d8.  It does not necessarily have to be a platonic solid number
diceCount = 4 #how many dice are rolled.  The system will take the best of this number - 1 of the rolls 

def getName():
    return "Thanger"

def getGender():
    return "male"

def getRace():
    return "half elf"

def getProfession():
    return "stone jumper failer"

def getAbilityMod(stat):
    if stat == 1:
        return '-5'
    elif stat <= 3:
        return '-4'
    elif stat <= 5:
        return '-3'
    elif stat <= 7:
        return '-2'
    elif stat <= 9:
        return '-1'
    elif stat <= 11:
        return '+0'
    elif stat <= 13:
        return '+1'
    elif stat <= 15:
        return '+2'
    elif stat <= 17:
        return '+3'
    elif stat <= 19:
        return '+4'
    elif stat <= 21:
        return '+5'
    elif stat <= 23:
        return '+6'
    elif stat <= 25:
        return '+7'
    elif stat <= 27:
        return '+8'
    elif stat <= 29:
        return '+9'
    else:
        return '+10'

def stats():
    stats = getStats()
    formattedStats = "Str: {0}\t({1})\nDex: {2}\t({3})\nCon: {4}\t({5})\nInt: {6}\t({7})\nWis: {8}\t({9})\nCha: {10}\t({11})".format(stats[0], getAbilityMod(stats[0]),
                                                                                                                                     stats[1], getAbilityMod(stats[1]),
                                                                                                                                     stats[2], getAbilityMod(stats[2]),
                                                                                                                                     stats[3], getAbilityMod(stats[3]),
                                                                                                                                     stats[4], getAbilityMod(stats[4]),
                                                                                                                                     stats[5], getAbilityMod(stats[5]))
    return formattedStats

def getNPC():
    print("Name: ", getName())
    print("Gender: ", getGender())
    print("Race: ", getRace())
    print("Profession:", getProfession())
    print("Stats:\n" + stats())
    print("")

def getInt(string):
    while True:
        try:
            val = int(string)
            if val <= 0:
                return 1
            else:
                return val
        except ValueError:
            return 1

def getStats():
    stats = []
    numToRoll = 6 #6 stats per character
    for i in range(0, numToRoll):
        sum = 0
        min = 99999999
        #this loop just adds all the rolls together, but records which number was smallest
        #after it runs, it subtracts that from the sum, which effectively is picking the best of the rolls
        for j in range(0, diceCount):
            val = rand(1, diceSize)
            sum += val
            if val < min:
                min = val
        sum -= min
        stats.append(sum)
    return stats

def main():
    while(True):
        line = input("Press enter to generate an NPC, or a number to get several. ")
        print("\n", end="")
        if line.lower() == "exit":
            break;
        num = getInt(line)
        for i in range(0, num):
            getNPC()

main()
