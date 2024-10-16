import sys
import subprocess

#  get args

args = sys.argv
print(args)

# ASSUMPTION: at least 1 argument (even if its an empty string) is passed to the python script (which it is)

user_input_split = args[1].split()
print(user_input_split)

function_passed = user_input_split[0]
description_passed = " ".join(user_input_split[1:])
print("description_passed: \""+description_passed+"\"")

# if you start a new entry while another one is already running, it will just change entries lol
if function_passed == "--start" or function_passed == "--change" or function_passed == "--toggle":
    subprocess.run(["./start_time_entry", description_passed])
    subprocess.run(["./notify", f"New entry started:\n{description_passed}"])
elif function_passed == "--now":
    now_subprocess = subprocess.run(["./get_toggl_now"], capture_output=True, text=True, check=True)
    # print("NOT PROCESS STDOUT: ", now_subprocess.stdout)
    output = now_subprocess.stdout
    lines = output.split("\n")
    # print("lines: ", lines)
    description_line = lines[0]
    duration_line = lines[2]
    description_split = description_line.split()
    description = (" ").join(description_split[:-1])
    print(description)
    duration_split = duration_line.split()
    duration = (" ").join(duration_split[1:])
    print(duration)
    subprocess.run(["./notify", description+"\n"+duration])
elif function_passed == "--stop":
    stop_process = subprocess.run(["./stop_and_return_output"], capture_output=True, text=True, check=True)
    output = stop_process.stdout.strip()
    subprocess.run(["./notify", "Stop: \n"+output])
else:
    subprocess.run(["./notify", "Unknown command.\nUse: --stop/--start [desc args]/--now"])