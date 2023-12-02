if __name__ == '__main__':
    count = 0
    try:
        while True:
            num = int(input("Enter a number\n"))
            if num < 0:
                print("Enter a positive number ")
                continue
            if num == 0:
                break

            dividables = []
            for dividers in range(1, num):
                if num % dividers == 0:
                    count = count + 1
                    dividables.append(dividers)
                else:
                    continue
            print("Entered number is ", num)
            print("This number can be divide", count, "times by these numbers", dividables)
    except Exception as e:
        print(e)
