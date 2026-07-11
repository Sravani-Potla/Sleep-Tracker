from datetime import datetime

print("===== SLEEP TRACKER =====")

sleep_time = input("Enter sleep time (HH:MM, e.g. 22:30): ")
wake_time = input("Enter wake-up time (HH:MM, e.g. 06:30): ")

sleep = datetime.strptime(sleep_time, "%H:%M")
wake = datetime.strptime(wake_time, "%H:%M")

# If wake-up time is on the next day
if wake <= sleep:
    from datetime import timedelta
    wake += timedelta(days=1)

duration = wake - sleep

hours = duration.seconds // 3600
minutes = (duration.seconds % 3600) // 60

print("\n===== SLEEP REPORT =====")
print("Sleep Time :", sleep_time)
print("Wake Time  :", wake_time)
print("Total Sleep:", hours, "hours", minutes, "minutes")

if hours >= 7 and hours <= 9:
    print("Sleep Status: Good Sleep 😊")
elif hours < 7:
    print("Sleep Status: Not Enough Sleep 😴")
else:
    print("Sleep Status: Too Much Sleep 💤")