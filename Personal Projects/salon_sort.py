#place = 0
alumnos = 0
totalcaracteresind = 0
totalcaracteres = 0
abcs = ["a", "b", "c",] 
lettercount = -1
linecount = 0
lista = ["Regina Aguirre Corvera", "Juan Carlos Arguelles Jaramillo", "Eugenia Berlanga García", "Regina Cabada Aguirre", "Monteserrat Cantú Silva", "Valentina Alejandra Guadalupe Durán Lozano", "Danna Paola Galarza López", "Sofía Daniela Garza Villarreal", "Lizbeth Valeria González Sepúlveda", "Gustavo Emanuel Guerra Gómez", "Verónica Iga Gutiérrez", "Sara López Quiroz", "André Millán Rivera",
         "Marcela Morales De la Garza", "Ana Paula Morales González", "Mónica Daniela Pedraza Galván", "María Fernanda Pérez Castillo", "Diego Alejandro Pérez Frías", "Maximiliano Roca Cavazos", "César Zahid Rosales", "María Fernanda Ruelas Reza", "Jorge Salazar Gaona", "Paulina Solis Cruz", "Isabella Tamez Cárdenas", "David Melchidek Tompkins Gómez", "Melissa Treviño García", "Luis Gabriel Zambrano Kunte"]

print(f"RESULTS FOR {abcs[0]}.")
for i in abcs:
	resultcount = 0
	lettercount += 1
	for person in lista:
		alumnos += 1 #iterates every element in list
		totalcaracteresind = 0
		for sample in person:
			totalcaracteresind += 1
			totalcaracteres += 1
			if sample == abcs[lettercount]:
				print(f"Result: '{sample}' found in {totalcaracteresind}th letter of {person} ")
				resultcount += 1
				

			#else:
				#print(f'"{abcs[lettercount]}" not found') #prints characters from list
			linecount += 1
	print(f'Letter result: La letra "{abcs[lettercount]}" apareció {resultcount} veces en total.')
	

#Resultados al final
print(f"Se analizaron {lettercount+1} letras.")
print(f"La lista de letras buscadas son: {abcs}.")

print(f"Hay {totalcaracteresind} alumnos en la lista.")
print(f"Hay {totalcaracteres} caracteres en total.")
#print(f'Final Result: "{abcs[0]}" se encontró {resultcount} veces en total.')
print(f"Se iteró la búsqueda {linecount} veces.")
	
	#else:
	#	print(f"Not found anywhere {count}.")

