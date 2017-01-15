from dynamic_programming.longest_common_subsequence import lcs
from dynamic_programming.longest_increasing_subsequence import lis

str1 = "abcfdcbab"
str2 = "acbgdcb"

print(lcs(str1, str2))

seq = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(lis(seq))
