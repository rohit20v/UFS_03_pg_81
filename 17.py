if __name__ == '__main__':
    word = "CIAO"
    letters = []
    index = 0

    while index < len(word):
        letter = input("Enter a letter\n")
        if letter.upper() == word[index]:
            letters.append(letter)
            index += 1

    print("You've added enough letter to make a ciao!\n", "".join(letters))
