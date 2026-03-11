day = (input("Enter a day: ")).lower()

if day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
     print("It's a working day")
elif day == "saturday" or day == "sunday":
     print("It's a weekend")
else:
     print("It's not a day")