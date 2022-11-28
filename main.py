print("Year to Minutes Converter")
year = int(input("Enter how many years: "),)

days = year * 365
hours = days * 24
minutes = hours * 60

if year > 1:
    print("In", year ,"years there are:")
else:
    print("In", year ,"year there are:")

print(days, "days\n",
      hours, "hours and\n",
      minutes, "minutes")