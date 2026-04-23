from color import light_blue
import os

def menu():
	print(light_blue("\n--- TODO APP ---"))
	print("1. Show tasks")
	print("2. Add task")
	print("3. Complete task(toggle)")
	print("4. Delete task")
	print("5. Edit task")
	print("6. Stats")
	print("7. Search task")
	print("8. Quit")

def clear():
	os.system("clear") # Mac/Linux
	# os.system("cls") # Windows (if needed)
