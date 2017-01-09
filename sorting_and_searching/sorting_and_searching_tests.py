from sorting_and_searching.binary_search import recursive_binary_search, iterative_binary_search

arr = [0, 1, 2, 3, 5, 8, 13, 21]
element = 8

print(recursive_binary_search(arr, element))
print(iterative_binary_search(arr, element))
element = 7
print(recursive_binary_search(arr, element))
print(iterative_binary_search(arr, element))
