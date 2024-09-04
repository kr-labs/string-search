def search_str(file_path, word):
    with open(file_path) as file:
        in_file = False
        lines = file.readlines()
        for line in lines:
            if line.find(word) != -1:
                print("Line {}: {}".format(lines.index(line), line))

user_input = input("Enter a word to search for in this text:\n")
user_file = input("Enter the directory of your file (if in project, begin with ./):\n")

search_str(user_file, user_input)