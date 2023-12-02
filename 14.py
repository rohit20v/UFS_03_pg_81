def multiplyList(l):
    res = 1
    for i in l:
        res = res * i
    return res


if __name__ == '__main__':
    multipliers = []
    sums = []
    while True:
        num = int(input("Enter a 0 if you dont wanna play anymore\nEnter a number if you keep wanna play\n"))
        if num == 0:
            break
        else:
            if num % 2 == 0:
                sums.append(num)
            else:
                multipliers.append(num)

    print("Even numbers inserted are: ", sums, "and their sum is: ", sum(sums), "\n",
          "Odd numbers inserted are: ", multipliers, "and their product is: ", multiplyList(multipliers))
