import os.path
from datetime import date
import re


def get_priorities_from_file():
    prior_dict = {}
    with open("priorities.txt") as input_string:
        for i in input_string.readlines():
            prior_dict[i.strip()] = 0

    return prior_dict


def write_priorities_to_file(prior_dict):
    pass


def load_day_routine(file_path):
    with open(file_path) as file:
        return file.readlines()


def write_case_to_file(case_dict):
    day = date.today().strftime("%y-%m-%d")
    filename = f"{day}.txt"
    file_path = os.path.join("days", filename)

    # Если файл существует - достаем содержимое и сортируем.
    # if os.path.exists(file_path):
    #     sort_cases(file_path)
    # else:
        #записываем
    with open(file_path, "at") as file:
        file.write(case_dict)
    sort_cases(file_path)
    return filename

#читает файл, сортирует строки по времени, записывает обратно в файл
def sort_cases(file_path):
    lines = []
    with open(file_path) as file:
        lines = [line for line in file.readlines() if len(line) > 7]
    lines = sorted(lines, key=lambda x: re.findall("\\d{2}:\\d{2}", x))

    with open(file_path, "wt") as file:
        for line in lines:
            file.write(line)
