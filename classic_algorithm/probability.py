from number_types import real


def probability(number):
    number = real(number)
    if 0 <= number <= 1:
        return number
    else:
        print()
        if number < 0:
            print("Error: Вероятность < 0")
        else:
            print("Error: Вероятность > 1")
        print("Повторите ввод")
        return probability(input())
