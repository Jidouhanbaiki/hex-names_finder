def is_valid_char(char):
    if char in ["a", "b", "c", "d", "e", "f"]:
        return True
    if char in ["i", "l", "g", "o", "s"]:
        return True
    return False


def check_word(word):
    if len(word) != 6:
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


# reading the file
eng_dict = []
with open("wordsEn.txt", "r") as vocab:
    for line in vocab:
        eng_dict.append(line[:-1])

#eng_dict = eng_dict[:200]
print(len(eng_dict))
#print(eng_dict)

outcome = []
for word in eng_dict:
    if check_word(word) is True:
        outcome.append(word)
print(len(outcome))

dict_changes = {"o":"0", "i":"1","l":"1", "s":"5", "g":"9"}
representation = []
for word in outcome:
    new_word = ""
    for char in word:
        if char in dict_changes.keys():
            new_word = new_word + dict_changes[char]
        else:
            new_word = new_word + char
    representation.append(new_word)


new_file = open("output.txt", "w")
output = "\n".join(representation)
new_file.write(output)
new_file.close()

print(len(representation))





