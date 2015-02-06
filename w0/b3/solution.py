def final_position(command_string, left_end, right_end):
    position = 0
    left_end = - left_end

    for command in command_string:
        if command == "L":
            if position > left_end:
                position = position - 1

        elif command in command_string:
            if position < right_end:
                position = position + 1

    return position