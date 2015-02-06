def reduce_file_path(path):
    
    str_len = len(path) 
    reduced_path = []
    reduced_path_postion = 0;
    path_str_position = 0
    while path_str_position < str_len:
        if path[path_str_position] == "/":
            reduced_path.append("/")
            
            
            path_str_position = path_str_position + 1
            if path_str_position < str_len:
                    break
            while path[path_str_position] == "/" :
                path_str_position = path_str_position + 1
                if path_str_position < str_len:
                    break

        elif path[path_str_position] == ".":
            path_str_position = path_str_position + 1
            if path[path_str_position] == ".":
                if len(reduced_path) > 1:
                    del reduced_path[len(reduced_path)-1]

        else:
            directory = ""
            while path[path_str_position] not in [".", "/"]:
                directory = directory + path[path_str_position]
                path_str_position = path_str_position + 1

    return "".join(reduced_path)





