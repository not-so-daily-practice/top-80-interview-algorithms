from sorting_and_searching.binary_search import recursive_binary_search, iterative_binary_search
from sorting_and_searching.search_sorted_and_rotated_array import search_rotated_array

arr = [0, 1, 2, 3, 5, 8, 13, 21]
element = 8

print(recursive_binary_search(arr, element))
print(iterative_binary_search(arr, element))

rotated_arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
element = 9
print(search_rotated_array(rotated_arr, element))
