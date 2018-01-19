"""
Kirkman's schoolgirl problem
"""
import json
from copy import deepcopy
import random
# girls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
girls = [i for i in range(1, 16)]
days = ["Sun", "Mon", "Tues", "Wed", "Thu", "Fri", "Sat"]
banned = {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: [5, 6], 5: [4, 6], 6: [5, 4], 7: [8, 9], 8: [
    9, 7], 9: [8, 7], 10: [11, 12], 11: [12, 10], 12: [10, 11], 13: [14, 15], 14: [15, 13], 15: [14, 13]}
# print(len(girls))
finalLst = []
for i in range(0, len(days)):
    toAppend = [days[i]]
    if i == 0:
        toTurn = girls.copy()
        for d in range(0, 15, 3):
            ls = [toTurn[d], toTurn[d + 1], toTurn[d + 2]]
            toAppend.append(ls)
        banned2 = deepcopy(banned)
    else:
        banned2 = deepcopy(banned)
        toTurn = girls.copy()
        random.shuffle(toTurn)
        # print(toTurn)
        for d in range(0, 15, 3):
            ls = [toTurn[d], toTurn[d + 1], toTurn[d + 2]]
            # print(d)
            # print("Hola")
            for j in ls:
                for b in range(0,len(banned2[j])):
                    print(b)
                    if j == banned2[j][b]:
                        d = 0
                        # print(ls)
                        # print(ls[c])
                        # print(banned2[j][b])
                        # print(banned2[j])
                        # print("----------")
                        random.shuffle(toTurn)
                        # print(toTurn)
                        banned2 = deepcopy(banned)
                        toAppend = [days[i]]
                    else:                        
                        banned2[j].append(j)
                        banned2[j] = list(set(banned2[j]))
                        toAppend.append(ls)
    finalLst.append(toAppend)
    banned = banned2
# print(json.dumps(finalLst, skipkeys=True, indent=4))
print(finalLst)
print("----")
print(banned)
