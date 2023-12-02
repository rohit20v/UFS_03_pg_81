if __name__ == '__main__':
    numbers = []

    sortedNumbers = list(range(1, 104, 4))

    while True:
        try:
            num = int(float(input("Enter a 0 if you dont wanna play anymore\nEnter a number: \n")))
            if num == 0:
                break
            else:
                numbers.append(num)
            if num is not sortedNumbers:
                for i in sortedNumbers:
                    if num < i:
                        sortedNumbers.insert(sortedNumbers.index(i), num)
                        break
            continue
        except ValueError as e:
            print("Input type is wrong")

    print("Numbers are ", numbers, "\n", "Played ", len(numbers), " times")
    print("Sorted list contains: ", len(sortedNumbers), "numbers!")
