#--- Validates Date ---

def valid_date(date):
	parts = date.split("/")

	if len(parts) != 3:
		return False

	month, day, year = parts

	if not (month.isdigit() and day.isdigit() and year.isdigit()):
		return False

	if not (1 <= int(month) <=12):
		return False

	if not(1 <= int(day) <= 31):
		return False

	return True
	
#--- Validates Priority ---

def valid_priority(priority):
	return priority.strip().lower() in ["high", "medium", "low"]


#--- Validates Index ---

def valid_index(num, tasks):
	return 1<= num <= len(tasks)
