'''
Write a function to check if two strings
are anagrams of each other
'''

def areAnagrams(string1, string2):
    import string
    for char in string.punctuation:
        # replace any punctuation symbol with empty character
        string1.replace(char, "")
        string2.replace(char, "")

        dict1 = dict()
        dict2 = dict()

        for i in string1:
            if (i in dict1):
                dict1[i] += 1
            else:
                dict1[i] = 1

        for j in string2:
            if (j in dict2):
                dict2[j] += 1
            else:
                dict2[j] = 1

        list1 = list(dict1.items())
        list2 = list(dict2.items())

        list1.sort()
        list2.sort()

        # for debugging
        # print(list1)
        # for debugging
        # print(list2)

        if(list1 == list2):
            return "The given strings are anagrams of each other."
        else:
            return "No, the given strings are not anagrams of each other."


    
string1 = "yesno"
string2 = "noyes"

print(areAnagrams(string1, string2));
