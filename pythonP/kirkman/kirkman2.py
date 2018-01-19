import copy
import random
banned = [[2, 3], [1, 3], [1, 2], [5, 6], [6, 4], [5, 4], [8, 9], [7, 9], [
    8, 7], [11, 12], [10, 12], [11, 10], [14, 15], [13, 15], [14, 13]]
girls = [i for i in range(1, 16)]
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
final = {}
for i in range(0, len(days)):
    final[days[i]] = []
# print(final)
for i in range(0, len(days)):
    if i == 0:
        appender = [[1, 2, 3], [4, 5, 6], [
            7, 8, 9], [10, 11, 12], [13, 14, 15]]
        final["Sun"] = appender
    else:
        appender = []
        copyl = girls.copy()
        random.shuffle(copyl)
        banned2 = copy.deepcopy(banned)
        for d in range(0, 15, 3):
            appender2 = [copyl[d], copyl[d + 1], copyl[d + 2]]
            good = True
            brk = False
            for n in appender2:
                for b in range(0, len(banned2[n - 1])):
                    for c in range(0, len(appender2)):
                        # print(appender2[c])
                        # print(banned2[n - 1][b])
                        if banned2[n - 1][b] == appender2[c]:
                            random.shuffle(copyl)
                            # appender = []
                            d = 0
                            banned2 = copy.deepcopy(banned)
                            break                    
                        else:
                            banned2[n - 1].append(appender2[c])
                            banned2[n - 1] = list(set(banned2[n-1]))
            appender.append(appender2)
            banned = copy.deepcopy(banned2)
        final[days[i]] = appender
print(final)
print(banned)
