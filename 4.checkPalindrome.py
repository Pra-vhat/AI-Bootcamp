'''
Check Palindrome
'''


def isPalindrome(string1):
    left = 0
    right = len(string1) - 1


    while left < right:
        if(string1[left] != string1[right]):
            return f"{string1} is not a palindrome"

        left += 1
        right -= 1

    return f"{string1} is a Palindrome"

string1 = "whattahw"
print(isPalindrome(string1))
