'''
Write a script which asks the user for one of four cardinal directions.
The user is expected to enter one of: north, south, east or west.
However, the letter case doesn't matter, so she may enter NORTH, North or nOrTh and they are all recognized as north.
According to the user's choice, the program outputs countries/areas neighboring Poland in that direction.
'''

direction = input("Prosze, wybierz jeden z czterech kierunkow geograficznych: " )

direction_low = direction.lower()

if direction_low == "polnoc":
	print("Na polnocy jest Morze Baltyckie i Obwod Kaliningradzki.")

elif direction_low == "poludnie":
	print("Na poludniu sa Czechy i Slowacja.")

elif direction_low == "wschod":
	print("Na wschodzie sa Ukraina, Bialorus i Litwa.")

elif direction_low == "zachod":
	print("Na zachodzie sa Niemcy.")

else:
	print("Nie ma takiego kierunku...")
