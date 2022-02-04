# 20CE029 Misari Gami
# GitHub repository link : https://github.com/MisariGami/Pra5/blob/main/20CE029_Pra5.py

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa. 

# Sample Input: HackerRank.com presents "Pythonist 2".

# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".


def swap_case(str):
    ans = ''
    for i in str:
        if i.isupper():
            ans += i.lower()
        elif i.islower():
            ans += i.upper()
        else:
            ans += i
    return ans

str = input()
print(swap_case(str))
