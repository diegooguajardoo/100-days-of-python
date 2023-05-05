
dictionary = [
	{
		"Alumno":"Nombre",
		"Salón":"Numero"
	}
]

def add_member(al, sal):
	new_member = {}
	new_member["Alumno"] = al
	new_member["Salón"] = sal
	dictionary.append(new_member)


while salon != "exit":
	salon = input("Matricula: ")
	alumno = input("Nombre del alumno: ")
	add_member(alumno,salon)
print(dictionary)