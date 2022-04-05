def format_name(fname,lname):
	fname = fname.title()
	lname = lname.title()
	return(f"{fname} {lname}")

first = input("What is your first name? ")
last = input("What is your last name? ")

result = format_name(first, last)
print(result)