print("############ String Manipulation Basics ############")

text = "The center() method center aligns a string. The alignment is done using a specified character (whitespace is the default)"

#center aligns
print(text.center(15,'#'))

#Prints the occurance of a string in a string variable
print("Total Occurances:",text.count('a'))
print("Total Occurances with a range:",text.count('a',0,len(text)))

#find returns lowest index and rfind returns the highest index
print("Index:",text.find('a'))
print("Index with range find:",text.find('a'))
print("Index with range rfind:",text.rfind('a',0,len(text)))

#changes case of a string
swapspace1 = "The swapcase() method returns a copy of the string with all its uppercase letters converted into lower case and vice versa."
print("swapspace1:",swapspace1.swapcase())

#The zfill() method adds zeros(0) at the beginning of the string. The length of the returned string depends on the width provided.
print("zfill(), padding zeros", '12345'.zfill(10))


allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

#Nested Dictionaires
def totalBrought(guests, item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
