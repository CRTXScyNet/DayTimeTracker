from datetime import time


def get_total_minutes(hours_minutes=time.min):
    return hours_minutes.hour*60+hours_minutes.minute

def get_difference_of_times_in_minutes(time1=time.min, time2=time.max):
    return abs(get_total_minutes(time1) - get_total_minutes(time2))

def convert_minutes_to_time(minutes):
    return time(minutes//60,minutes%60)
