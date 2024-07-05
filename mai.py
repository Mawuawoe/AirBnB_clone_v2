#!/usr/bin/python3
import inspect
import io
import sys
import cmd

"""
 Cleanup file storage
"""
import os
file_path = "file.json"
if not os.path.exists(file_path):
    try:
        from models.engine.file_storage import FileStorage
        file_path = FileStorage._FileStorage__file_path
    except:
        pass
if os.path.exists(file_path):
    os.remove(file_path)


import console

"""
 Create console
"""
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False

"""
 Exec command
"""
def exec_command(my_console, the_command, last_lines = 1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])

"""
 Tests
"""
state_name = "California"
result = exec_command(my_console, "create State name=\"{}\"".format(state_name))
if result is None or result == "":
    print("FAIL: No ID retrieved")
state_id = result

city_name = "San Francisco is super cool"
result = exec_command(my_console, "create City state_id=\"{}\" name=\"{}\"".format(state_id, city_name.replace(" ", "_")))
if result is None or result == "":
    print("FAIL: No ID retrieved")
city_id = result

result = exec_command(my_console, "show City {}".format(city_id))
if result is None or result == "":
    print("FAIL: empty output")
if "[City]" not in result or city_id not in result:
    print("FAIL: wrong output format: \"{}\"".format(result))
if "name" not in result or city_name not in result:
    print(city_name)
    print(result)
    print("FAIL: missing new information: \"{}\"".format(result))
if "state_id" not in result or state_id not in result:
    print("FAIL: missing new information: \"{}\"".format(result))
print("OK", end="")
