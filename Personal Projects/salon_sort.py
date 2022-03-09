place = 0
character = ["a", "b", "c"] 
salon = ["Regina Aguirre Corvera", "Juan Carlos Arguelles Jaramillo", "Eugenia Berlanga García", "Regina Cabada Aguirre", "Monteserrat Cantú Silva", "Valentina Alejandra GuadalupeDurán Lozano", "Danna Paola Galarza López", "Sofía Daniela Garza Villarreal", "Lizbeth Valeria González Sepúlveda", "Gustavo Emanuel Guerra Gómez", "Verónica Iga Gutiérrez", "Sara López Quiroz", "André Millán Rivera",
         "Marcela Morales De la Garza", "Ana Paula Morales González", "Mónica Daniela Pedraza Galván", "María Fernanda Pérez Castillo", "Diego Alejandro Pérez Frías", "Maximiliano Roca Cavazos", "César Zahid Rosales", "María Fernanda Ruelas Reza", "Jorge Salazar Gaona", "Paulina Solis Cruz", "Isabella Tamez Cárdenas", "David Melchidek Tompkins Gómez", "Melissa Treviño García", "Luis Gabriel Zambrano Kunte"]
for letter in salon[place]:
	try:
		if letter == "l":
			print(f"Result: '{letter}' found in {place}")
			break
		else:
			place += 1
	except:
		print("Not found anywhere.")

