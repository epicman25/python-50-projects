import time
from time import strftime,gmtime
minutes,seconds = map(int,input("Please enter the timer in format(mm:ss):").split(":"))

total_seconds = (minutes*60) + seconds
remaining_seconds = total_seconds
current_time = int(time.time())
target_time = current_time + total_seconds
print(time.strftime("%H:%M:%S"))
while current_time!= target_time:
    current_time+=1
    remaining_seconds -=1
    time.sleep(1)
    remiaing_time_minutes = remaining_seconds//60
    remiaing_time_seconds = remaining_seconds%60
    print(f"remaining || {remiaing_time_minutes}:{remiaing_time_seconds}")
    print(time.strftime("%H:%M:%S"))

print("=======================")
print(time.strftime("%H:%M:%S"))


print("TIMER UPPPPPPPPP")





