from functions import convert_time_in_seconds, time_format_validation, sleep_cycles

running = True
total_hours = 0
total_minutes = 0

while running:
    going_to_bed_time = input("What time would you prefer to go to bed? (Provide in hh:mm format)\n")
    try:
        total_hours, total_minutes = convert_time_in_seconds(going_to_bed_time)
        time_format_validation(going_to_bed_time)
        running = False
    except ValueError:
        incorrect_format_error_message = 'The format is provided is not correct or the provided value'
        print(incorrect_format_error_message)
        continue

print("The following hours are perfect to wake up according to the sleep cycles:")
sleep_cycles(total_hours, total_minutes)
