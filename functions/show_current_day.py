from datetime import time
from functions.load_write_functions import load_day_routine , get_priorities_from_file , sort_cases
from functions.time_converter import get_difference_of_times_in_minutes
from functions.time_converter import convert_minutes_to_time

def show_day_info(file_name):
    custom_format = "%H часов %M минут"

    begin_time = time.min
    end_time = time.min
    last_time = time.min

    priority_dict = get_priorities_from_file()

    filename = f"days/{file_name}"
    sort_cases(filename)
    file = load_day_routine(filename)

    for string in file:
        if "::" not in string:
            continue

        priority = ""

        # разбиваем строку на дело и время окончания
        business, time_ = string.strip().split("::")
        time_ = time.fromisoformat(time_)

        # Вытаскиваем приоритет
        if "!" in business:
            priority, business = business.split("!")

        # Проверка типа дела по словарю
        for prior, amount in priority_dict.items():
            if prior in priority.lower():
                priority_dict[prior] += get_difference_of_times_in_minutes(last_time, time_)

        if begin_time == time.min:
            begin_time = time_
        if end_time < time_:
            end_time = time_

        last_time = time_

        print(f"В {time_.strftime(custom_format)} закончил {business}.")

    print()

    difference = get_difference_of_times_in_minutes(begin_time, end_time)
    percent = 100
    for prior, val in priority_dict.items():
        if val != 0:
            converted_time = convert_minutes_to_time(val).strftime(custom_format)
            percentage = round(val / difference * 100)
            percent -= percentage
            print(f"На '{prior}' ушло {converted_time}, это {percentage}% от записанного времени.")

    print(f"Всего вы бодрствовали {convert_minutes_to_time(difference).strftime(custom_format)}.")

    if percent > 1:
        print(f"{percent}% не учтено.")
