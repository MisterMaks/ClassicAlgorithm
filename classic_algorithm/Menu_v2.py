# import pandas as pd
import time

from number_types import real, positive, natural
from probability import probability
from check_filename import check_filename
from fitness_all_type_types import check_fitness_all_type_types as check_fit_types


class Menu_of_classic_genetic_algorithm:

    def __init__(self, task_dict):

        self.task_dict = task_dict

        self.common_options = [{"n_iter": 50, "type": "natural"}, {"eps": 0.5, "type": "positive"},
                               {"fitness_all_type": "max", "type": "fit"},
                               {"parent_selection_type": "something", "type": "str"},
                               {"cross_type": "something", "type": "str"},
                               {"p_cross": 0.5, "type": "probability"},
                               {"mutation_type": "something", "type": "str"},
                               {"p_mutation": 0.1, "type": "probability"},
                               {"size_of_population": 50, "type": "natural"}]

        self.functions_for_type = {"float": float, "int": int, "str": str,
                                   "probability": probability, "positive": positive,
                                   "natural": natural, "real": real, "filename": check_filename,
                                   "fit": check_fit_types}

        self.unpack_common_options()

        # Дополнительные возможности для разработчика!!! Работа данного блока кода не предусмотрена!!!

        """
        self.functions_for_type.update({"dataset": self.read_dataset, "matrix": self.read_matrix})
        """

        if self.check_types_options() is "Error":
            return None

        self.task_dict_full = self.task_dict
        self.task_dict_full["options"] = self.common_options + self.task_dict_full["options"]

        time.sleep(1)

        self.input_data()
        print("SUCCESSFUL")
        self.unpack_options()
        self.unpack_task_with_options()

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

            time.sleep(0.1)

            input_data = input()
            if input_data == "" and option_key in list(self.dict_common_options.keys()):
                input_data = str(self.task_dict_full["options"][option][option_key])
                self.task_dict_full["options"][option][option_key] = function(input_data)
                print(self.task_dict_full["options"][option][option_key])
            elif input_data == "":
                input_data = str(self.task_dict_full["options"][option][option_key])
                self.task_dict_full["options"][option][option_key] = function(input_data)
            else:
                self.task_dict_full["options"][option][option_key] = function(input_data)
            print("-" * len(message))

            print()

        return None

    def unpack_options(self):
        self.options = {}
        for option in self.task_dict["options"]:
            option_key = list(option.keys())[0]
            option_value = option[option_key]
            self.options[option_key] = option_value
        return None

    def unpack_common_options(self):
        self.dict_common_options = {}
        for option in self.common_options:
            option_key = list(option.keys())[0]
            option_value = option[option_key]
            self.dict_common_options[option_key] = option_value
        return None

    def unpack_task_with_options(self):
        self.task_with_options = {}
        self.task_with_options["task"] = self.task_dict_full["task"]
        self.task_with_options.update(self.options)
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
