# #/////Example One
# sum =0
# sum += 1
# sum += 2
# sum += 3
# sum += 4
# print(sum)

# #/////Example Two
# sum = 1 + \
#     2 + \
#     3 + \
#     4
# print(sum)

# #/////Example Three
# sum = (
#     1 +
#     2 +
#     3 +
#     4)
# print(sum)

# #/////Example Four
# disaster = True
# if disaster:
#     print("Whoa!")
# else:
#     print("Whee!")


# #/////Example Five
# furry = False
# large = False
# if furry:
#     if large:
#         print("It's a yeti!")
#     else:
#         print("It's a cat!")
# else:
#     if large:
#         print("It's a whale!")
#     else:
#         print("It's a human. Or a hairless cat.")

#/////Truthie & Falsie
some_list = []
if some_list:
    print("There's something in here.")
else:
    print("Hey! It's empty!")

#///// Multiple Comparisons
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, "is a vowel!")
else:
    print(letter, "is not a vowel!")

#/////Check vowel-ness pythonically
vowels = "aeiou"
letter = "o"
letter in vowels

#/////Vowel-set
letter = "o"
vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(letter in vowel_set)

#/////Vowel-list
vowel_list = ['a', 'e', 'i', 'o', 'u']
print(letter in vowel_list)

#/////Vowel-tuple
vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(letter in vowel_tuple)

#/////Vowel-dict
vowel_dict = {'a': 'apple', 'e': 'elephant', 'i': 'impala', 'o': 'ocelot', 'u': 'unicorn'}
print(letter in vowel_dict)

vowel_string = "aeiou"
letter in vowel_dict

