from task import Task
from storage import load_tasks, save_tasks, show_tasks, sort_tasks, add_task, complete_task, delete_task, edit_task, show_stats, search_task
from color import red
from ui import menu, clear

#--- Main Menu ---

def main():
	tasks = load_tasks()

	while True:
		clear()
		menu()
		choice = input("Choose: ")

		if choice == "1":
			show_tasks(tasks)
			input("\nPress Enter to continue...")
		elif choice == "2":
			add_task(tasks)
		elif choice == "3":
			complete_task(tasks)
		elif choice == "4":
			delete_task(tasks)
		elif choice == "5":
			edit_task(tasks)
		elif choice == "6":
			show_stats(tasks)
			input("\nPress Enter to continue...")
		elif choice == "7":
			search_task(tasks)
		elif choice == "8":
			break
		else:
			print(red("Invalid choice!"))

if __name__ == "__main__":
	main()
