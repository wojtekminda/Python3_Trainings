import datetime

print("Czesc! W ktorym roku sie urodziles?")
year_of_birth = input()

if not year_of_birth.isdigit():
    print("To nie rok")
    
year_of_birth_int = int(year_of_birth)

age = datetime.datetime.now().year - year_of_birth_int

if age <= 0:
    print("Klamiesz...")
else:
    print("Masz ", age, "lat :)")
