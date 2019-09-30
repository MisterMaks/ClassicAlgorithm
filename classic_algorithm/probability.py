from number_types import real


def probability(number):
    number = real(number)
    if 0 <= number <= 1:
        return number
    else:
        print()
        if number < 0:
            print("Error: {} < 0".format(number))
        else:
            print("Error: {} > 1".format(number))
        print("Повторите ввод")
        return probability(input())
