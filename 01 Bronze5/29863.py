sleep_time = int(input())
alarm_time = int(input())

if sleep_time <= alarm_time:
    sleep_hours = alarm_time - sleep_time
else:
    sleep_hours = 24 - (sleep_time - alarm_time)

print(sleep_hours)
