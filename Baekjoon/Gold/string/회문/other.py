# 해당 코드 블로그: https://velog.io/@jungeun/%EB%B0%B1%EC%A4%80-17609-%ED%9A%8C%EB%AC%B8-python-%ED%92%80%EC%9D%B4

import sys

input = sys.stdin.readline

T = int(input())

def is_palindrome(word):
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            rm_left = word[left+1:right+1]
            if rm_left == rm_left[::-1]:
                return 1

            rm_right = word[left:right]
            if rm_right == rm_right[::-1]:
                return 1

            return 2

        left += 1
        right -= 1

    return 0

for _ in range(T):
    word = input().rstrip()
    diff = is_palindrome(word)
    print(diff)