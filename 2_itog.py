def again():
    global number
    global result
    print("Введите число от 3 до 20: ")
    number = int(input())
    result = []

    if number <= 20 and number >= 3:
        for n in range(1, number):
            for m in range(1, number):
                if number % (n+m) == 0 and n < m:
                    result.append(n)
                    result.append(m)

        print(number, " - ", *result, sep = "")
    else:
        again()

again()