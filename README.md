# Classic Algorithm

## Скачайте zip архив, там все файлы

![](https://github.com/MisterMaks/ClassicAlgorithm/blob/master/images/instruction_img.png) 

## Для работы вам понадобятся файлы из папки 'classic_algorithm': 
* 'Menu.py'
* 'number_types.py'
* 'check_filename.py'
* 'fitness_all_type_types.py'
* 'probability.py' 
* 'list_options.py'

## Пример работы программы вы можете увидеть здесь, ниже, или в папке 'classic_algorithm', файл 'Launch_Menu_v2.ipynb'

# Импортируем класс для чтения вводимых данных: Menu_of_classic_genetic_algoritm


```python
from Menu_v2 import Menu_of_classic_genetic_algorithm as menu
```

# Класс принимает на вход словарь в формате:
## {"task": "(Название задачи)", "options": [{"(Название параметра 1)": None, "type": "(Тип данных для этого параметра)"}, {"(Название параметра 2)": None, "type": "(Тип данных для этого параметра)"}]}

* Есть поддержка значений по умолчанию, тогда вместо 'None' пишите значение по умолчанию. В этом случае, если вы ничего не вводите и нажимаете Enter, то будет значение по умолчанию. 

# Поддерживаемые типы данных:

1. real - вещественные числа
2. positive - положительные числа
3. natural - натуральные числа
4. probability - тип для вероятностей, число принадлежит диапозону [0, 1]
5. filename - тип для файлов, если нужно работать с файлами, то функция проверит, что файл существует
6. str - используется для строковых значений
7. Также есть поддержка основных типов int, float - если будете их использовать, то ошибки и невалидные данные обрабатывайте сами!!!

** Типы данных указываются в словаре в кавычках

# Дополнительные возможности
В "type" можно передать список. Например: {... "type": [1, 2, 3]}.
Тогда будет появляться меню с вариантами из этого списка. В этом случае пользователь будет ограничен вариантами из этого списка. В качестве значения по умолчанию можно установить значение из этого списка, но если пользователь выбирает какой-то из вариантов, то он должен написать номер этого варианта. В итоговые значения записывается выбранный вариант.

# Примеры словарей для "Отбора признаков" и "Коммивояжера"


```python
feature_selection = {"task": "feature_selection", "options": [{"dataset": None, "type": "filename"}]}
travelling_salesman = {"task": "travelling_salesman", "options": [{"n_cities": None, "type": "natural"}, 
                                                                  {"matrix": None, "type": "filename"}]}
```

# Пример работы программы


```python
menu = menu(travelling_salesman)
```

    Введите 'n_iter':
    
    50
    -----------------
    
    Введите 'eps':
    
    0.5
    --------------
    
    Введите 'fitness_all_type':
    
    max
    ---------------------------
    
    Введите 'parent_selection_type':
    
    something
    --------------------------------
    
    Введите 'cross_type':
    
    something
    ---------------------
    
    Введите 'p_cross':
    
    0.5
    ------------------
    
    Введите 'mutation_type':
    
    something
    ------------------------
    
    Введите 'p_mutation':
    
    0.1
    ---------------------
    
    Введите 'size_of_population':
    
    50
    -----------------------------
    
    Введите 'n_cities':
    
    
    Error: None - не число!
    Повторите ввод
    10
    -------------------
    
    Введите имя файла для 'matrix'
    hint: (файл должен находиться в текущей директории):
    
    
    Файл 'None' не найден! Попробуйте еще раз!
    test.csv
    -----------------------------------------------------------------------------------
    
    SUCCESSFUL


# Вывод словаря с введенными значениями


```python
# Созданный словарь
menu.task_dict_full
```




    {'task': 'travelling_salesman',
     'options': [{'n_iter': 50, 'type': 'natural'},
      {'eps': 0.5, 'type': 'positive'},
      {'fitness_all_type': 'max', 'type': 'fit'},
      {'parent_selection_type': 'something', 'type': 'str'},
      {'cross_type': 'something', 'type': 'str'},
      {'p_cross': 0.5, 'type': 'probability'},
      {'mutation_type': 'something', 'type': 'str'},
      {'p_mutation': 0.1, 'type': 'probability'},
      {'size_of_population': 50, 'type': 'natural'},
      {'n_cities': 10, 'type': 'natural'},
      {'matrix': 'test.csv', 'type': 'filename'}]}




```python
# Cловарь с параметрами данной задачи
menu.options
```




    {'n_iter': 50,
     'eps': 0.5,
     'fitness_all_type': 'max',
     'parent_selection_type': 'something',
     'cross_type': 'something',
     'p_cross': 0.5,
     'mutation_type': 'something',
     'p_mutation': 0.1,
     'size_of_population': 50,
     'n_cities': 10,
     'matrix': 'test.csv'}




```python
# Словарь, в котором есть задача и ее параметры 
menu.task_with_options
```




    {'task': 'travelling_salesman',
     'n_iter': 50,
     'eps': 0.5,
     'fitness_all_type': 'max',
     'parent_selection_type': 'something',
     'cross_type': 'something',
     'p_cross': 0.5,
     'mutation_type': 'something',
     'p_mutation': 0.1,
     'size_of_population': 50,
     'n_cities': 10,
     'matrix': 'test.csv'}



# Примеры словарей для "Отбора признаков" и "Коммивояжера" со значениями по умолчанию


```python
feature_selection_with_def_val = {"task": "feature_selection", 
                                  "options": [{"dataset": "wine.csv", "type": "filename"}]}
travelling_salesman_with_def_val = {"task": "travelling_salesman", 
                                    "options": [{"n_cities": 10, "type": "natural"}, 
                                                {"matrix": "test.csv", "type": "filename"}]}
```

# Пример работы программы для значений по умолчанию
## Я ничего не ввожу, просто нажимаю Enter


```python
menu_for_def_val = menu(feature_selection_with_def_val)
```

    Введите 'n_iter':
    
    50
    -----------------
    
    Введите 'eps':
    
    0.5
    --------------
    
    Введите 'fitness_all_type':
    
    max
    ---------------------------
    
    Введите 'parent_selection_type':
    
    something
    --------------------------------
    
    Введите 'cross_type':
    
    something
    ---------------------
    
    Введите 'p_cross':
    
    0.5
    ------------------
    
    Введите 'mutation_type':
    
    something
    ------------------------
    
    Введите 'p_mutation':
    
    0.1
    ---------------------
    
    Введите 'size_of_population':
    
    50
    -----------------------------
    
    Введите имя файла для 'dataset'
    hint: (файл должен находиться в текущей директории):
    
    wine.csv
    ------------------------------------------------------------------------------------
    
    SUCCESSFUL


# Тестовый пример, для демонстрации передачи списка в "type"


```python
test_task = {"task": "test_task", "options": [{"test_option": None, "type": [11, 22, 33]}]}
```


```python
test_menu = menu(test_task)
```

    Введите 'n_iter':
    
    50
    ----------------------
    
    Введите 'eps':
    
    0.5
    ----------------------
    
    Введите 'fitness_all_type':
    
    max
    ----------------------
    
    Введите 'parent_selection_type':
    
    something
    ----------------------
    
    Введите 'cross_type':
    
    something
    ----------------------
    
    Введите 'p_cross':
    
    0.5
    ----------------------
    
    Введите 'mutation_type':
    
    something
    ----------------------
    
    Введите 'p_mutation':
    
    0.1
    ----------------------
    
    Введите 'size_of_population':
    
    50
    ----------------------
    
    Выберете 'test_option'
    (hint: нужно ввести номер варианта):
        1. 11
        2. 22
        3. 33
    
    1
    
    1. 11
    ----------------------
    
    SUCCESSFUL



```python
# Созданный словарь
test_menu.task_dict_full
```




    {'task': 'test_task',
     'options': [{'n_iter': 50, 'type': 'natural'},
      {'eps': 0.5, 'type': 'positive'},
      {'fitness_all_type': 'max', 'type': 'fit'},
      {'parent_selection_type': 'something', 'type': 'str'},
      {'cross_type': 'something', 'type': 'str'},
      {'p_cross': 0.5, 'type': 'probability'},
      {'mutation_type': 'something', 'type': 'str'},
      {'p_mutation': 0.1, 'type': 'probability'},
      {'size_of_population': 50, 'type': 'natural'},
      {'test_option': 11, 'type': [11, 22, 33]}]}



## Тестовый пример, для демонстрации передачи списка в "type" со значением по умолчанию


```python
test_task_with_def_val = {"task": "test_task", "options": [{"test_option": 11, "type": [11, 22, 33]}]}
```


```python
test_menu_with_def_val = menu(test_task_with_def_val)
```

    Введите 'n_iter':
    
    50
    ----------------------
    
    Введите 'eps':
    
    0.5
    ----------------------
    
    Введите 'fitness_all_type':
    
    max
    ----------------------
    
    Введите 'parent_selection_type':
    
    something
    ----------------------
    
    Введите 'cross_type':
    
    something
    ----------------------
    
    Введите 'p_cross':
    
    0.5
    ----------------------
    
    Введите 'mutation_type':
    
    something
    ----------------------
    
    Введите 'p_mutation':
    
    0.1
    ----------------------
    
    Введите 'size_of_population':
    
    50
    ----------------------
    
    Выберете 'test_option'
    (hint: нужно ввести номер варианта):
        1. 11
        2. 22
        3. 33
    
    
    11
    ----------------------
    
    SUCCESSFUL



```python
# Созданный словарь
test_menu_with_def_val.task_dict_full
```




    {'task': 'test_task',
     'options': [{'n_iter': 50, 'type': 'natural'},
      {'eps': 0.5, 'type': 'positive'},
      {'fitness_all_type': 'max', 'type': 'fit'},
      {'parent_selection_type': 'something', 'type': 'str'},
      {'cross_type': 'something', 'type': 'str'},
      {'p_cross': 0.5, 'type': 'probability'},
      {'mutation_type': 'something', 'type': 'str'},
      {'p_mutation': 0.1, 'type': 'probability'},
      {'size_of_population': 50, 'type': 'natural'},
      {'test_option': 11, 'type': [11, 22, 33]}]}




```python

```
