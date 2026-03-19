from task import Task
from storage import load_tasks, save_tasks, show_tasks, sort_tasks, add_tasks, complete_tasks, delete_tasks, edit_tasks, show_stats, search_tasks
from color import red
from ui import menu

#--- Main Menu ---

def main():
	tasks = load_tasks()

	while True:
		menu()
		choice = input("Choose: ")

		if choice == "1":
			show_tasks(tasks)
		elif choice == "2":
			add_tasks(tasks)
		elif choice == "3":
			complete_tasks(tasks)
		elif choice == "4":
			delete_tasks(tasks)
		elif choice == "5":
			edit_tasks(tasks)
		elif choice == "6":
			show_stats(tasks)
		elif choice == "7":
			search_tasks(tasks)
		elif choice == "8":
			break
		else:
			print(red("Invalid"))

if __name__ == "__main__":
	main()
