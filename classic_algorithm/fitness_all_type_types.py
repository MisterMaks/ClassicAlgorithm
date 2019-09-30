def check_fitness_all_type_types(type):
    types = ["min", "max", "mean"]
    if type not in types:
        print()
        print("Error: Невалидный тип!")
        print("Повторите ввод")
        return check_fitness_all_type_types(input())
    return type