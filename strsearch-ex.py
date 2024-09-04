def search_str(file_path, word):
    # Opens file given by the user input
    with open(file_path) as file:
        lines = file.readlines()
        # Iterate through each line in the text
        for line in lines:
            # Finds the word specified by the user
            if line.find(word) != -1:
                print("Line {}: {}".format(lines.index(line), line))

user_input = input("Enter a word to search for in this text:\n")
user_file = input("Enter the directory of your file (if in project, begin with ./):\n")

search_str('example.txt', 'ERROR')