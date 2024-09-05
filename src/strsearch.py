# Kevin R: STRING-SEARCH 2024

def search_str(file_path, word):
    try:
        file = open(file_path, "r")
        lines = file.readlines()
        instances = 0

        print("In file located in: {}\n".format(file_path))
        for line in lines:
            if line.find(word) != -1:
                instances += 1
                print("Line {}: {}".format(lines.index(line) + 1, line))
        
        if instances > 0:
            print("\nNumber of instaces found: {}".format(instances))
        else:
            print("No number of instances found!")
        file.close()

    except FileNotFoundError:
        print("File does not exist.")

user_file = input("Enter the file with directory (if in project directory, begin with ./):\n")
user_input = input("Enter a word to search for in file:\n")

search_str(user_file, user_input)