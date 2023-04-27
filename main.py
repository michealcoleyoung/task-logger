import time
import pyperclip
from datetime import datetime

tasks = []

while True:
    task = input("What are you working on? Type 'export data' to export your data: ")
    if task.lower() == "export data":
        output = ""
        for t in tasks:
            output += f"{t['start_time']} {t['date']} {t['task']} Time Worked: {t['time_worked']} \n"
        print(output)
        pyperclip.copy(output)
    else:
        start_time = time.strftime("%I:%M:%S %p", time.localtime())
        date = time.strftime("%m/%d/%Y", time.localtime())
        print(f"Task '{task}' started at {start_time} on {date}")
        input("Press 'Enter' to stop the timer and record time worked... ")
        end_time = time.strftime("%I:%M:%S %p", time.localtime())
        start = datetime.strptime(start_time, "%I:%M:%S %p")
        end = datetime.strptime(end_time, "%I:%M:%S %p")
        total_time = end - start
        time_worked = str(total_time).split(".")[0]
        tasks.append({"start_time": start_time, "date": date, "task": task, "time_worked": time_worked})
        print(f"Task '{task}' ended at {end_time} on {date}. Time worked: {time_worked}\n")