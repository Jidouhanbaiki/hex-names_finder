import sys

VERSION = "1.0"


def is_valid_char(char):
    """
    Check if there is an available hex equivalent for a character.
    :param char: input character
    :return: boolean
    """
    if char in ["a", "b", "c", "d", "e", "f"]:
        return True
    if char in ["i", "l", "g", "o", "s"]:
        return True
    return False


def check_word(word):
    """
    Make sure we can transform this word into the hex-equivalent.
    :param word: input word
    :return: boolean
    """
    if len(word) < 2:
        return False
    for char in word:
        if is_valid_char(char) is False:
            return False
    has_char_i = False
    if "i" in word:  # no both i and l in the same words
        has_char_i = True
    if "l" in word and has_char_i:
        return False
    return True


def hex_finder(any_length=False, comparison=0, char_count=6):
    """
    The main procedure of the module.
    :param any_length: boolean, if true then we do not check the length at all
    :param comparison: can be -1, 0 and 1.
        if -1 then we are looking for words with the length less than char_count value;
        if 0 then we are looking for words with the exact char_count value;
        if 1 then we are looking for words longer than char_count value;
    :param char_count: number of characters if the word. Cannot be lower than 2.
    :return: string with all the name divided by \n.
    """

    # read English lexicon from the file
    eng_dict = []
    with open("wordsEn.txt", "r") as vocab:
        for line in vocab:
            eng_dict.append(line[:-1])

    # generate a list of words which correspond to our conditions
    outcome = []
    for word in eng_dict:
        can_add = False
        if not any_length:
            if comparison == -1:
                if len(word) < char_count:
                    can_add = True
            elif comparison == 0:
                if len(word) == char_count:
                    can_add = True
            elif comparison == 1:
                if len(word) > char_count:
                    can_add = True
            else:
                raise NotImplementedError("Wrong comparison value! Comparison argument should equal to -1, 0 or 1.")
        else:
            can_add = True
        if can_add:
            if check_word(word) is True:
                outcome.append(word)

    dict_changes = {"o": "0", "i": "1", "l": "1", "s": "5", "g": "9"}

    # transform the words in their hex version
    representation = []
    for word in outcome:
        new_word = ""
        for char in word:
            if char in dict_changes.keys():
                new_word += dict_changes[char]
            else:
                new_word = new_word + char
        representation.append(new_word)

    print("Output: " + str(len(representation)) + " words found and transformed.")
    return "\n".join(representation)


def write_to_file(content, filename="output.txt"):
    new_file = open(filename, "w")
    new_file.write(content)
    new_file.close()
    print("Output saved to: " + filename)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        any_length = False
        comparison = 0
        char_count = 6
        file_name = "output.txt"
        for argument in sys.argv:
            if argument in ['-h', '-help']:
                print()
                print("Welcome to hex-words finder!")
                print("List of available commands:")
                print("    -h -- help")
                print("    -v -- version")
                print("    -any -- disable word filter")
                print("    [any number from 2 to 12 inclusive] -- mention the exact count of character in word. Default is 6.")
                print("    -more -- leave all words with more characters than specified by the user (exclusive).")
                print("    -less -- leave all words with less characters than specified by the user (exclusive).")
                print("    [any word with '.' in it] -- the name of output file. Default name is 'output.txt'.")
                sys.exit(0)
            if argument in ['-v', '-version', '-ver']:
                print()
                print("Welcome to hex-words finder!")
                print("Version: " + VERSION)
                sys.exit(0)
            if argument in ['-any']:
                any_length = True
            if argument in ['-more']:
                comparison = 1
            if argument in ['-less']:
                comparison = -1
            if argument in ['-equals']:
                comparison = 0
            try:
                if int(argument) in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
                    char_count = int(argument)
            except ValueError:
                pass
            if "." in argument:
                file_name = argument

        write_to_file(hex_finder(any_length, comparison, char_count), file_name)

    else:
        write_to_file(hex_finder())