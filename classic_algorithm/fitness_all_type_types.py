def check_fitness_all_type_types(type_fit):
    types_fit = ["min", "max", "mean"]
    if type_fit not in types_fit:
        print()
        print("Error: {} - невалидный тип!".format(type_fit))
        print("hint: Введите 'max', 'min', 'mean'")
        print("Повторите ввод")
        return check_fitness_all_type_types(input())
    return type_fit
