def magic_string(string):
    moves_needed = 0
    middle = len(string) // 2
    
    for char in range(middle):
        if string[char] == "<":
            moves_needed += 1
    
    for char in range(middle, len(string)):
        if string[char] == ">":
            moves_needed += 1
    
    return moves_needed