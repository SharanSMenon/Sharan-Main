import copy
import random
from functools import lru_cache
banned = {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [5, 6], 5: [
    4, 6], 6: [5, 4], 7: [8, 9], 8: [7, 9], 9: [8, 7]}
#, 10: [11, 12], 11: [10, 12], 12: [11, 10], 13: [14, 15], 14: [13, 15], 15: [14, 13]
final = {}
girls = [i for i in range(1, 10)]
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
print(girls)
for q in range(0, len(days)):
    final[days[q]] = []
# def insert(number,key):
#     global

# @lru_cache(maxsize=10000)


def check(l):
    banned2 = copy.deepcopy(banned)
    for n in l:
        for b in range(0, len(banned2[n])):
            for c in range(0, len(l)):
                if banned2[n][b] == l[c]:
                    return [False]
                else:
                    if n != l[c]:
                        banned2[n].append(l[c])
    return [True, banned2]
for i in range(0, len(days)):
    if i == 0:
        appender = [[1, 2, 3], [4, 5, 6], [
            7, 8, 9], [10, 11, 12], [13, 14, 15]]
        final['Sun'] = appender
    else:
        numbers = []
        copyg = girls.copy()
        # banned2 = copy.deepcopy(banned)
        toKeep = []
        random.shuffle(copyg)
        for d in range(0, len(copyg), 3):
            threes = [copyg[d], copyg[d + 1], copyg[d + 2]]
            print(copyg)
            print("-----")
            print(toKeep)
            while check(threes)[0] == False:
                random.shuffle(copyg)
                ch = check(threes)
                if ch[0] == True:
                    print("u")
                    banned = copy.deepcopy(ch[1])
                    break
            toKeep.append(threes)
            for h in range(0, len(threes)):
                index = copyg.index(threes[h])
                copyg.pop(index)
        final[days[i]] = toKeep
print(final)
