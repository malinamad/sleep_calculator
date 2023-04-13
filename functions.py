from datetime import datetime

seconds_in_hour = 3600
seconds_in_minute = 60


def convert_time_in_seconds(time):
    hours = int(time[:2]) * seconds_in_hour
    minutes = int(time[-2:]) * seconds_in_minute
    return hours, minutes


def time_format_validation(date_text):
    time_format = '%H:%M'

    if date_text == datetime.strptime(date_text, time_format).strftime(time_format):
        pass


def reduce_hour_value_to_zero(hours):
    if hours // seconds_in_hour >= 24:
        hours = 0
    return hours


def add_minutes_time_to_hour(hours, minutes):
    if minutes // seconds_in_minute >= seconds_in_minute:
        hours += seconds_in_hour
        hours = reduce_hour_value_to_zero(hours)
        minutes = minutes - seconds_in_minute * seconds_in_minute
    return hours, minutes


def adjust_time_to_midnight(hours, minutes):
    hours = reduce_hour_value_to_zero(hours)
    hours, minutes = add_minutes_time_to_hour(hours, minutes)
    return hours, minutes


def convert_time_to_print(hours, minutes):
    conv_hours = hours // seconds_in_hour
    conv_minutes = minutes // seconds_in_minute
    return str(conv_hours), str(conv_minutes)


def sleep_cycles(hours, minutes, cycles_amount=6):
    for _ in range(cycles_amount):
        sleep_cycle_hours = 3600
        sleep_cycle_minutes = 1800

        hours += sleep_cycle_hours
        minutes += sleep_cycle_minutes
        hours, minutes = adjust_time_to_midnight(hours, minutes)

        converted_hours, converted_minutes = convert_time_to_print(hours, minutes)

        if len(converted_hours) == 1 and len(converted_minutes) == 1:
            print(f'0{converted_hours}:0{converted_minutes}')
            continue
        if len(converted_hours) == 1:
            print(f'0{converted_hours}:{converted_minutes}')
            continue
        if len(converted_minutes) == 1:
            print(f'{converted_hours}:0{converted_minutes}')
            continue

        print(converted_hours + ':' + converted_minutes)
