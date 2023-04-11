from datetime import datetime

going_to_bed_time = input("What time would you prefer to go to bed? (Provide in hh:mm format)\n")

# need validation
hours = int(going_to_bed_time[:2]) * 3600
minutes = int(going_to_bed_time[-2:]) * 60
sleep_cycle_hours = 3600
sleep_cycle_minutes = 1800


def time_format_validation(date_text):
    try:
        if date_text == datetime.strptime(date_text, "%H:%M").strftime('%H:%M'):
            pass
            # perhaps while loop
    except Exception:
        print("The format is provided is not correct")


time_format_validation(going_to_bed_time)

print("The following hours are perfect to wake up according to the sleep cycles:")

for _ in range(6):
    hours += sleep_cycle_hours
    minutes += sleep_cycle_minutes
    if hours // 3600 >= 24:
        hours = 0
    if minutes // 60 >= 60:
        hours += 1 * 3600
        minutes = minutes - 60 * 60

    print(str(hours // 3600) + ":" + str(minutes // 60))
