def reduce_file_path(path):
    path_parted = path.split("/")
    output_path = []

    for path_element in path_parted:
        if path_element == "..":
            if len(output_path) > 0:
                output_path.pop()
                
        elif path_element not in [".", "/", ""]:
            output_path.append(path_element)

    output_path = "/" + "/".join(output_path)

    return output_path




