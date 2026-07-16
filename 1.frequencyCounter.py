# Frequency Counter:
'''
Write a function that counts 
the frequency of words in a paragraph and 
returns the top 3 most common words.
'''

def top_three_words(paragraph):
    # first split the paragraph string
    # then register each word into a list


    # but first
    # this removes any periods from the paragraph
    # paragraph = paragraph.replace(".", "")

    # and many other symbols...
    # paragraph = paragraph.replace("?", "")
    # paragraph = paragraph.replace("!", "")
    # paragraph = paragraph.replace("\"", "")

    # Or you can just do this
    import string
    for char in string.punctuation:
        paragraph = paragraph.replace(char, "")

        
    paragraph = paragraph.lower()

    words = list(paragraph.split());
    count = dict();
    for i in range(len(words)):
        if words[i] in count:
            count[words[i]] += 1
        else:
            count[words[i]] = 1

    count =  list(count.items())
    count.sort(key = lambda x: x[1], reverse = True)

    # print(count)

    if len(count) >= 3:
        return(count [:3])
    else:
        return("No three unique words.")


example1 = "red blue red blue red blue green"
print(example1)
print(top_three_words(example1))
print()

example2 = "The cat sat on the mat. The cat is happy. The cat likes the mat."
print(example2)
print(top_three_words(example2))
print()

example3 = "dog cat dog bird cat dog fish"
print(example3)
print(top_three_words(example3))
print()





