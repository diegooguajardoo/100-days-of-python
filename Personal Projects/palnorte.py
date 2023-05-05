from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Hora actual: ", current_time)

parcels = datetime(2022,4,2,20,15,00)
print(parcels)

