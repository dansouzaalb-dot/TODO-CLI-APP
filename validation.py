from datetime import datetime

#--- Validates Date ---

def valid_date(date):
	try:
		datetime.strptime(date, "%m/%d/%Y")
		return True
	except ValueError:
		return False
	
#--- Validates Priority ---

def valid_priority(priority):
	return priority.strip().lower() in ["high", "medium", "low"]


#--- Validates Index ---

def valid_index(num, tasks):
	return 1<= num <= len(tasks)
