import os
from datetime import datetime, date


from functions.load_write_functions import get_priorities_from_file, write_case_to_file
from re import match

def enter_new_case():
    loaded_dict = get_priorities_from_file()
    again = True
    file_name = ""
    while True:

        today = date.today().strftime("%y-%m-%d")
        is_weekday_exists = os.path.exists("days\\" + today+".txt")
        is_weekend_exists = os.path.exists("days\\" + today+".txt")


        tag = ""
        while True:
            print("Напиши тег из доступных:")
            print(", ".join([k for k in loaded_dict.keys()]))
            tag = input()
            tags = [ i for i in loaded_dict.keys() if tag.lower() in i]
            if len(tags) != 0 and len(tag.strip()) != 0:
                tag = tags[0]
                break
            if tag not in loaded_dict.keys():
                print("Оставить без тега? \n да/нет")
                if input().lower() == "да":
                    tag = ""
                    break

        answer = "ss"
        case = ""
        while answer.lower() not in "да":
            print("Введи дело:")
            case = input()
            print("Ты уверен? \n да/нет")
            answer = input()

        time_ = ""
        while not match("\\d{2}:\\d{2}", time_) and time_.lower() != "сейчас":
            print("Введи время в которое закончил в формате ##:## или 'сейчас', чтобы ввести текущее время:")
            time_ = input()
            if time_.lower() == "сейчас":
                time_ = datetime.now().strftime("%H:%M")


        print("Ты ввел занятие", f"с таким тегом: {tag}" if tag !="" else "без тега")
        print(f"Собственно занятие: {case}")
        print(f"Закончил в {time_}")

        if tag == "":
            case_sequence = f"{case}::{time_}\n"
        else:
            case_sequence = f"{tag.strip()}!{case}::{time_}\n"

        file_name = write_case_to_file(case_sequence)

        print()
        again = input("Нажмите 'enter' чтобы закончить\n")
        if again == "" :
            break
        print()


    print("Всего доброго")
    return file_name