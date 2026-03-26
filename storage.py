# -*- coding: utf-8 -*-
import json
from validation import valid_date, valid_priority, valid_index
from color import red, green, color
from task import Task

FILE = "tasks.json"


#--- Load Tasks ---

def load_tasks():
	try:
		with open(FILE, "r") as f:
			data = json.load(f)

		return [Task(d["date"], d["title"], d["priority"], d["done"]) for d in data]

	except FileNotFoundError:
		return []

#--- Save Tasks ---

def save_tasks(tasks):
	data = []

	for task in tasks:
		data.append({
			"date": task.date,
			"title": task.title,
			"priority": task.priority,
			"done": task.done
		})

	with open(FILE, "w") as f:
		json.dump(data, f, indent =4)

#--- Show Tasks ---

def show_tasks(tasks):
	if not tasks:
		print(red("\nNo tasks."))
		return

	sort_tasks(tasks)

	print("\nPending tasks:")
	for i, task in enumerate(tasks, 1):
		if not task.done:
			task.display(i)

	print("\nCompleted tasks:")
	for i, task in enumerate(tasks, 1):
		if task.done:
			task.display(i)

#--- Filter: Date tasks ---

def sort_tasks(tasks):
	tasks.sort(key = lambda task: task.date)

#--- Add tasks ---

def add_tasks(tasks):
	title = input("New task: ")
	
	date = input("Date(mm/dd/yyyy): ")
	if valid_date(date):
		pass
	else:
		print(red("ERROR! mm/dd/yyyy"))
		return
	priority = input("Urgency(HIGH, MEDIUM or LOW): ")
	if valid_priority(priority):
		pass
	else:
		print(red("ERROR! Either: High, Medium or Low"))
		return
	tasks.append(Task(date, title, priority))
	sort_tasks(tasks)
	save_tasks(tasks)
	print(green("Task added."))

#--- Completes and ✔️ tasks ---

def complete_tasks(tasks):
	show_tasks(tasks)
	
	if not tasks:
		return

	try:
		num = int(input("Task number: "))
	except ValueError:
		print(red("ERROR! Please enter a number."))
		return

	if valid_index(num, tasks):
		tasks [num - 1].mark_done()
		sort_tasks(tasks)
		save_tasks(tasks)
		print(green("Task completed."))	
	else:
		print("Invalid number.")

#--- Delete tasks ---

def delete_tasks(tasks):
	show_tasks(tasks)

	if not tasks:
		return
	
	try:
		num = int(input("Task number to delete: "))
	except ValueError:
		print(red("ERROR! Please enter a number."))
		return

	if valid_index(num, tasks):
		removed = tasks.pop(num - 1)
		save_tasks(tasks)
		print(green("Removed:"), removed.title)
	else:
		print(red("ERRO! Invalid number."))

#--- Edit tasks ---

def edit_tasks(tasks):
	show_tasks(tasks)

	if not tasks:
		return
	try:
		num = int(input("Task number to edit: "))
	except ValueError:
		print(red("ERROR! Please enter a number."))
		return

	if valid_index(num, tasks):
		title = input("New title: ")
		date = input("New date(mm/dd/yyyy): ")
		if valid_date(date):
			pass
		else:
			print(red("ERROR! mm/dd/yyyy"))
			return

		priority = input("New urgency(HIGH, MEDIUM or LOW): ")
		if valid_priority(priority):
			pass
		else:
			print(red("ERROR! High, Medium or Low"))
			return
		tasks [num - 1].title = title
		tasks [num - 1].date = date
		tasks [num - 1].priority = priority
		sort_tasks(tasks)
		save_tasks(tasks)
		print(green("Task edited."))
	else:
		print(red("Invalid number."))

#--- Stats ---

def show_stats(tasks):
	total = len(tasks)
	completed = sum(task.done for task in tasks)
	pending = total - completed
	high_priority = sum(1 for task in tasks if task.priority.lower() == "high")
	medium_priority = sum(1 for task in tasks if task.priority.lower() == "medium")
	low_priority = sum(1 for task in tasks if task.priority.lower() == "low")

	print("\nStats")
	print("Total:", total)
	print("Pending:", pending, "Urgencies - HIGH:", high_priority, "MEDIUM:", medium_priority, "LOW:", low_priority)
	print("Completed:",completed)

#--- Search tasks ---

def search_tasks(tasks):
	
	if not tasks:
		print(red("\nNo tasks."))
		return

	keyword = input("Search task: ").lower()
	found = False

	for task in tasks:
		if keyword in task.title.lower():
			print(green(task))
			found = True
	
	if not found:
		print(red("Task not found!"))

