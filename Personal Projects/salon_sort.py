#place = 0
alumnos = 0
count2 = 0
abcs = ["a", "b", "c"] 
resultcount = 0
lista = ["Regina Aguirre Corvera", "Juan Carlos Arguelles Jaramillo", "Eugenia Berlanga García", "Regina Cabada Aguirre", "Monteserrat Cantú Silva", "Valentina Alejandra GuadalupeDurán Lozano", "Danna Paola Galarza López", "Sofía Daniela Garza Villarreal", "Lizbeth Valeria González Sepúlveda", "Gustavo Emanuel Guerra Gómez", "Verónica Iga Gutiérrez", "Sara López Quiroz", "André Millán Rivera",
         "Marcela Morales De la Garza", "Ana Paula Morales González", "Mónica Daniela Pedraza Galván", "María Fernanda Pérez Castillo", "Diego Alejandro Pérez Frías", "Maximiliano Roca Cavazos", "César Zahid Rosales", "María Fernanda Ruelas Reza", "Jorge Salazar Gaona", "Paulina Solis Cruz", "Isabella Tamez Cárdenas", "David Melchidek Tompkins Gómez", "Melissa Treviño García", "Luis Gabriel Zambrano Kunte"]

for person in lista:
	alumnos += 1 #iterates every element in list
	count2 = 0
	for sample in person:
		count2 += 1
		for character in sample:
			if character == abcs[0]:
				print(f"Result: '{character}' found in {count2}th letter of {person} ")
				resultcount += 1

			else:
				print(f'"{abcs[0]}" not found') #prints characters from list
	

#Resultados
print(f"Hay {alumnos} alumnos en la lista.")
print(f"Hay {count2} caracteres en total.")
print(f"La lista de letras buscadas son: {abcs}.")
print(f'Final Result: "{abcs[0]}" se encontró {resultcount} veces en total.')
	
	#else:
	#	print(f"Not found anywhere {count}.")

