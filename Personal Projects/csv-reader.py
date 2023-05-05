from csv import reader

with open("lista202.csv", "r") as read_obj:
	csv_reader = reader(read_obj)
	documento = list(csv_reader)

row_number = 2
col_number = 1
documento[row_number - 1][col_number - 1] = "Re"
value = documento[row_number - 1][col_number - 1]

print('Value in cell at 3rd row and 2nd column : ', value)
