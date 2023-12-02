
if __name__ == '__main__':
    count = []

    while True:
        try:
            num = int(float(input("Enter a 0 if you dont wanna play anymore\nEnter a number: \n")))
            # if num == '*':
            if num == 0:
                break
            else:
                count.append(num)
        except ValueError as e:
            print("Input type is wrong")

    print("Numbers are ", count, "\n", "Played ", len(count), " times")
