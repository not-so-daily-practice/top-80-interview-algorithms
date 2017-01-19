from strings_and_arrays.all_palindromic_partitions import all_palindromic_partitions
from strings_and_arrays.reverse_array_except_special import reverse_except_special

test_string = "a!!!b.c.d,e'f,ghi"

print(reverse_except_special(test_string))

test_string = "nitin"
print(all_palindromic_partitions(test_string))

test_string = "geeks"
print(all_palindromic_partitions(test_string))
