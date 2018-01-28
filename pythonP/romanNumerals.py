#Can convert roman numerals up to 5000
impValues = {'I':1,'II':2,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
lsSr = []
sTr = ''
n = 0
def roman():
    global impValues, lsSr, n, sTr
    nums = list(impValues.keys())
    ints = list(impValues.values())
    nNums = []
    nInts = []
    for i in range(0,len(ints)):
        if n > ints[i]:
            nNums.append(nums[i])
            nInts.append(ints[i])
        if n == ints[i]:
            lsSr.append(nums[i])
            return lsSr
    if n > 0 and n != 1 and n != 2:
        n = n - nInts[-1]
        lsSr.append(nNums[-1])
        retrn = roman()
    if n == 1:
        n = 2
n = int(input("Enter a number: "))
roman()
for i in range(0,len(lsSr)):
    sTr += lsSr[i]
print("Number in roman: ",sTr)
