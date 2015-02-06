#solve problem whit Uppercase - they shoudn't be count
def count_substrings(haystack, needle):
    
    count = 0
    pointer_needle = 0

    for haystack_position in range(0, len(haystack)):
        if haystack[haystack_position] == needle[pointer_needle]:
            pointer_needle = pointer_needle +1
            if pointer_needle == len(needle):
                count = count + 1
                pointer_needle = 0

    return count
