import itertools
n = 0
alumnos = 0
totalcaracteresind = 0
abcs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
abcs2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
letteriter1 = -1
letteriter2 = -1
linecount = 0
chartot = 0
letrasunicas = []
personasunicas = []
resultcount = 0
lista = ["Regina Aguirre Corvera", "Juan Carlos Arguelles Jaramillo", "Eugenia Berlanga García", "Regina Cabada Aguirre", "Monteserrat Cantú Silva", "Valentina Alejandra Guadalupe Durán Lozano", "Danna Paola Galarza López", "Sofía Daniela Garza Villarreal", "Lizbeth Valeria González Sepúlveda", "Gustavo Emanuel Guerra Gómez", "Verónica Iga Gutiérrez", "Sara López Quiroz", "André Millán Rivera",
         "Marcela Morales De la Garza", "Ana Paula Morales González", "Mónica Daniela Pedraza Galván", "María Fernanda Pérez Castillo", "Diego Alejandro Pérez Frías", "Maximiliano Roca Cavazos", "César Zahid Rosales", "María Fernanda Ruelas Reza", "Jorge Salazar Gaona", "Paulina Solis Cruz", "Isabella Tamez Cárdenas", "David Melchidek Tompkins Gómez", "Melissa Treviño García", "Luis Gabriel Zambrano Kunte"]
lista2 = ["Victoria Aguayo Sepúlveda","Amelie Balderrama Ramírez","Anabella Bueno","Geovani Gamaliel Camarillo Castro","María Fernanda Castillo Navarro","Mariangela De León Martínez","Jesús Gerardo De León Rivera","Alejandro Elizondo Peña","Jimena Flores","Renata García Morales","Eunise Victoria González Villarreal","Emilio González Álvarez","Ángela Regina Gutiérrez Arredondo","Nicole Dominick Jaubert Martínez","Jimena Lara Leija","Daniel de Jesús Maldonado Rodríguez","Salvador Muñoz Lavin","Daniela Ortega Martínez","Narcedalia Perales Lozano","Jimena María Peña Treviño","Valeria Pérez Estrada","Mariana Quiroz Hernández","Barbara Rodríguez de la Torre","Eugenia Ruiz Ransom","Mariangela Astrea Salinas Flores","Carlos Alonso Serroque Palacios","Paulina Silva Rivera"]
listastr = ["Regina Aguirre Corvera", "Juan Carlos Arguelles Jaramillo", "Eugenia Berlanga García", "Regina Cabada Aguirre", "Monteserrat Cantú Silva", "Valentina Alejandra Guadalupe Durán Lozano", "Danna Paola Galarza López", "Sofía Daniela Garza Villarreal", "Lizbeth Valeria González Sepúlveda", "Gustavo Emanuel Guerra Gómez", "Verónica Iga Gutiérrez", "Sara López Quiroz", "André Millán Rivera",
            "Marcela Morales De la Garza", "Ana Paula Morales González", "Mónica Daniela Pedraza Galván", "María Fernanda Pérez Castillo", "Diego Alejandro Pérez Frías", "Maximiliano Roca Cavazos", "César Zahid Rosales", "María Fernanda Ruelas Reza", "Jorge Salazar Gaona", "Paulina Solis Cruz", "Isabella Tamez Cárdenas", "David Melchidek Tompkins Gómez", "Melissa Treviño García", "Luis Gabriel Zambrano Kunte"]

for i in abcs:
	letteriter1 += 1
	print(f"RESULTS FOR {abcs[letteriter1]}.")
	if resultcount == 1:
		personasunicas.append(personaunica)
		lista.remove(personaunica)
	resultcount = 0
	
	
	personaiter = -1
	for person in lista:
		totalcaracteresind = 0
		personaiter += 1
		if letteriter1 == 0:
			chartot = len(person) + chartot


		for sample in person:
			totalcaracteresind += 1
			linecount += 1
			
			if sample.lower() == abcs[letteriter1]:
				#print(f"Result: '{sample}' found in {totalcaracteresind}th letter of {person} ")
				resultcount += 1
				personaunica = person	
			
	if resultcount == 1:
		letrasunicas.append(abcs[letteriter1])
		#print(personaiter)
		#personasunicas.append(lista[personaiter])
			#else:
				#print(f'"{abcs[lettercount]}" not found') #prints characters from list

		
		
	#print(f'Letter result: La letra "{abcs[letteriter1]}" apareció {resultcount} veces en total.\n')

for i in abcs:
	letteriter2 = 0
	letteriter1 += 1
	for j in abcs:
		mix = abcs[letteriter1] + abcs2[letteriter2]
		letteriter2 += 1
		print(mix)






#Resultados al final
print(f"Se analizaron {len(abcs)} letras.")
print(f"La lista de letras buscadas son: {abcs}.")
print(f"Hay {len(lista)} alumnos en la lista.")
print(f"Hay {chartot} caracteres en total.")
#print(f'Final Result: "{abcs[0]}" se encontró {resultcount} veces en total.')
print(f"Se iteró la búsqueda {linecount} veces.")

#Resultados de análisis
for i in letrasunicas:
	#print(personasunicas)
	print(f"{personasunicas[0 + n]} tiene la letras {letrasunicas[0 + n]}")
	print(f"Letras Unicas {letrasunicas[0 + n]}")
	n += 1

print(f"lista: {lista}")
	#else:
	#	print(f"Not found anywhere {count}.")

