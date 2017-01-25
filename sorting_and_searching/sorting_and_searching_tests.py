from sorting_and_searching.binary_search import recursive_binary_search
from sorting_and_searching.bubble_sort import bubble_sort
from sorting_and_searching.search_sorted_and_rotated_array import search_rotated_array

print("--------------------------------\n")
print("Recursive Binary Search")
arr = [0, 1, 2, 3, 5, 8, 13, 21]
element = 8
print(recursive_binary_search(arr, element))

print("--------------------------------\n")
print("Search Rotated Array")
rotated_arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
element = 9
print(search_rotated_array(rotated_arr, element))

print("--------------------------------\n")
print("Bubble Sort")
arr = [5, 1, 4, 2, 8]
print(bubble_sort(arr))
