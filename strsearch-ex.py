def search_str(file_path, word):
    # try block of code to verify that the file_path is a valid path to a file
    try:
        # open the file with read-only mode
        file = open(file_path, "r")
        lines = file.readlines()
        # used to find number of instances found of the word
        instances = 0

        print("In file located in: {}\n".format(file_path))
        # iterate through each line of the file
        for line in lines:
            if line.find(word) != -1:
                instances += 1
                print("Line {}: {}".format(lines.index(line) + 1, line))
        # check if there were any instances of the word foun in the file
        if instances > 0:
            print("\nNumber of instaces found: {}".format(instances))
        else:
            print("No number of instances found!")
        file.close()
    # if given file_path is not valid
    except FileNotFoundError:
        print("File does not exist.")

user_file = input("Enter the file with directory (if in project directory, begin with ./):\n")
user_input = input("Enter a word to search for in file:\n")

# utilizing example information
search_str("./example.txt", "ERROR")