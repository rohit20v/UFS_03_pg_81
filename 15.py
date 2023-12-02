if __name__ == '__main__':

    print("Enter 2 numbers\n")
    num1 = int(input())
    num2 = int(input())

    count = 0
    while True:
        if num1 < 0 or num2 < 0:
            print("Enter a positive number")
            break
        elif num1 > num2:
            while num1 > num2:
                num1 = num1 - num2
                count = count + 1
                print("Count: ", count, "big num: ", num1)
                break
        else:
            while num2 > num1:
                num2 = num2 - num1
                count = count + 1
                print("Count: ", count, "big num: ", num2)
                break

    # print("Count: ", count)

