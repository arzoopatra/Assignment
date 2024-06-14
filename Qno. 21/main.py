def count_occurrences(lst, element):  # sourcery skip: remove-unnecessary-cast
    count = sum(bool(item == element)
            for item in lst)
    return count

# Test the function
my_list = [1, 2, 3, 4, 1, 2, 1, 3, 1]
element_to_count = 1
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list.")
