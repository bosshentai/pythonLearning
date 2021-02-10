import datetime
birth_year = input('what year were you born? ')

today = datetime.date.today()
year_updated = today.year
your_age = int(year_updated) - int(birth_year)

print(f'Your age is {your_age}')

