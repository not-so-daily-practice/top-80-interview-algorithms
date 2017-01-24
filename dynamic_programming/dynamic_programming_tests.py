from dynamic_programming.edit_distance import edit_distance
from dynamic_programming.longest_common_subsequence import lcs
from dynamic_programming.longest_increasing_subsequence import lis

print("Longest Common Subsequence")

str1 = "abcfdcbab"
str2 = "acbgdcb"

print(lcs(str1, str2))

print("--------------------------------\n")
print("Longest Increasing Subsequence")

seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(lis(seq))

print("--------------------------------\n")
print("Edit Distance")

str_1 = "geek"
str_2 = "gesek"
print(edit_distance(str_1, str_2))

str_1 = "cat"
str_2 = "cut"
print(edit_distance(str_1, str_2))

str_1 = "sunday"
str_2 = "saturday"
print(edit_distance(str_1, str_2))
