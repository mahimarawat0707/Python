import time
import winsound

alarm_time = input("Enter the alarm time (HH:MM:SS, 24-hour format): ")

print("Waiting for alarm time...")

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Wake up!")
        winsound.Beep(1000, 1000)
        break
    time.sleep(1)