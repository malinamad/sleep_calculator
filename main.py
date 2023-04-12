from datetime import datetime

going_to_bed_time = input("What time would you prefer to go to bed? (Provide in hh:mm format)\n")

seconds_in_hour = 3600
seconds_in_minute = 60

# need validation
def convert_time_in_seconds(time):
    incorrect_value_error_message = 'Provide number values, not text!'
    try:
        hours = int(time[:2]) * seconds_in_hour
        minutes = int(time[-2:]) * seconds_in_minute
        return hours, minutes
    except ValueError:
        print(incorrect_value_error_message)

def time_format_validation(date_text):
    time_format = '%H:%M'
    incorrect_format_error_message = 'The format is provided is not correct or the provided value'
    try:
        if date_text == datetime.strptime(date_text, time_format).strftime(time_format):
            pass
            # perhaps while loop
    except ValueError:
        print(incorrect_format_error_message)


total_hours, total_minutes = convert_time_in_seconds(going_to_bed_time)
time_format_validation(going_to_bed_time)

print("The following hours are perfect to wake up according to the sleep cycles:")

for _ in range(6):
    sleep_cycle_hours = 3600
    sleep_cycle_minutes = 1800

    total_hours += sleep_cycle_hours
    total_minutes += sleep_cycle_minutes
    if total_hours // seconds_in_hour >= 24:
        total_hours = 0
    if total_minutes // seconds_in_minute >= seconds_in_minute:
        total_hours += seconds_in_hour
        if total_hours // seconds_in_hour >= 24:
            total_hours = 0
        total_minutes = total_minutes - seconds_in_minute * seconds_in_minute

    if len(str(total_hours // seconds_in_hour)) == 1 and len(str(total_minutes // seconds_in_minute)) == 1:
        print('0' + str(total_hours // seconds_in_hour) + ':0' + str(total_minutes // seconds_in_minute))
        continue
    if len(str(total_hours // seconds_in_hour)) == 1:
        print('0' + str(total_hours // seconds_in_hour) + ':' + str(total_minutes // seconds_in_minute))
        continue
    if len(str(total_minutes // seconds_in_minute)) == 1:
        print(str(total_hours // seconds_in_hour) + ':0' + str(total_minutes // seconds_in_minute))
        continue

    print(str(total_hours // seconds_in_hour) + ':' + str(total_minutes // seconds_in_minute))
