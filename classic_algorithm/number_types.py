def real(number):
    number_lst = list(map(str, list(range(10)))) + [".", "+", "-", "e"]
    for i in number:
        if i not in number_lst:
            print()
            print("Error: Это не число!")
            print("Повторите ввод")
            return real(input())
    try:
        return float(number)
    except ValueError:
        print()
        print("Error: Это не число!")
        print("Повторите ввод")
        return real(input())


def positive(number):
    number = real(number)
    if number > 0:
        return number
    else:
        print()
        print("Error: Число <= 0")
        print("Повторите ввод")
        return positive(input())


def whole(number):
    number = real(number)
    if number - int(number) == 0:
        return int(number)
    else:
        print()
        print("Error: Нецелое число")
        print("Повторите ввод")
        return whole(input())


def natural(number):
    number = real(number)
    if number > 0 and number - int(number) == 0:
        return int(number)
    else:
        print()
        print("Error: Ненатуральное число")
        print("Повторите ввод")
        return natural(input())
