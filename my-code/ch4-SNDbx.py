#/////Example One
sum =0
sum += 1
sum += 2
sum += 3
sum += 4
print(sum)

#/////Example Two
sum = 1 + \
    2 + \
    3 + \
    4
print(sum)

#/////Example Three
sum = (
    1 +
    2 +
    3 +
    4)
print(sum)

#/////Example Four
disaster = True
if disaster:
    print("Whoa!")
else:
    print("Whee!")


#/////Example Five
furry = False
large = False
if furry:
    if large:
        print("It's a yeti!")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat.")