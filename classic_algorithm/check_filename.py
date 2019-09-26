import os.path


def check_filename(filename):
    full_file_path = "./" + filename
    if os.path.isfile(full_file_path):
        return filename
    else:
        print()
        print("Файл не найден! Попробуйте еще раз!")
        return check_filename(input())
