#--- Create class Task ---

class Task:
	def __init__(self, date, title, priority, done = False):
		self.date = date
		self.title = title
		self.priority = priority.lower()
		self.done = done

	def mark_done(self):
		self.done = not self.done

	def __str__(self):
		status = "✔"if self.done else " "
		return f"[{status}] ({self.date}) {self.title} | Urgency: {self.priority}"

	def display(self, index):
		print(f"{index}. {self}")
