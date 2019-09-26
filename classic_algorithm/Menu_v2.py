# import pandas as pd
# import time

from number_types import real, positive, natural
from probability import probability
from check_filename import check_filename


class Menu_of_classic_genetic_algorithm:

    def __init__(self, task_dict):

        self.task_dict = task_dict

        self.common_options = [{"n_iter": None, "type": "natural"}, {"eps": None, "type": "positive"},
                               {"fitness_all_type": None, "type": "str"},
                               {"parent_selection_type": None, "type": "str"},
                               {"cross_type": None, "type": "str"}, {"p_cross": None, "type": "probability"},
                               {"mutation_type": None, "type": "str"},
                               {"p_mutation": None, "type": "probability"},
                               {"size_of_population": None, "type": "natural"}]

        self.functions_for_type = {"float": float, "int": int, "str": str,
                                   "probability": probability, "positive": positive,
                                   "natural": natural, "real": real, "filename": check_filename}

        # Дополнительные возможности для разработчика!!! Работа данного блока кода не предусмотрена!!!

        """
        self.functions_for_type.update({"dataset": self.read_dataset, "matrix": self.read_matrix})
        """

        if self.check_types_options() is "Error":
            return None

        self.task_dict_full = self.task_dict
        self.task_dict_full["options"] = self.common_options + self.task_dict_full["options"]

        self.input_data()

    def check_types_options(self):
        for option in self.task_dict["options"]:
            if option["type"] not in self.functions_for_type.keys():
                print()
                print("Ошибка типа данных! Проверьте типы!!!")
                return "Error"
        return None

    def input_data(self):
        option_key = 0
        for option in range(len(self.task_dict_full["options"])):
            option_key = list(self.task_dict_full["options"][option].keys())[0]
            type_of_data = self.task_dict_full["options"][option]["type"]
            function = self.functions_for_type[type_of_data]

            if type_of_data is "filename":
                message = ("Введите имя файла для '{}'\n" +
                           "hint: (файл должен находиться в текущей директории):").format(option_key)
            else:
                message = "Введите '{}':".format(option_key)

            print(message)

            # time.sleep(0.0001)

            while True:
                try:
                    input_data = input()
                    self.task_dict_full["options"][option][option_key] = function(input_data)
                    break
                except ValueError:
                    print()
                    print("Ошибка! Данные не валидны")
                    print("Повторите ввод")
                    print()
                    print(message)
                    continue
            print()

        return None

    # Дополнительные возможности для разработчика!!! Работа данного блока кода не предусмотрена!!!

    """                            
    def read_dataset(self, filename):
        full_file_path = "./" + filename
        try:
            dataset = pd.read_csv(full_file_path)
        except FileNotFoundError:
            print()
            print("Файл не найден! Попробуйте еще раз!")
            filename = input()
            return self.read_dataset(filename)

        pd.options.display.max_columns = 5
        pd.options.display.max_rows = 5

        print()
        print(dataset.head())

        return dataset


    def read_matrix(self, filename):
        full_file_path = "./" + filename

        try:
            matrix = pd.read_csv(full_file_path, header=None, sep=";").values.tolist()
        except FileNotFoundError:
            print()
            print("Файл не найден! Попробуйте еще раз!")
            filename = input()
            return self.read_matrix(filename)

        print()
        print(matrix)

        return matrix
    """
