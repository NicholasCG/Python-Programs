month = input("Input your month of birth").lower()
day = int(input("Input your day of birth")

if( month == "march" and day >= 21) or( month == "april" and day <= 19):
	print("Your zodiac sign is Aries")
elif( month == "april" and day >= 20) or( month == "may" and day <= 20):
	print("your zodiac sign is Taurus")
elif( month == "may" and day >= 21) or( month == "june" and  day <= 20):
	print("Your zodiac sign is Gemini")
elif( month == "june" and day  >= 21) or( month == "july" and day <= 22):
	print("Your zodiac sign is Cancer")
elif( month == "july" and day >= 23) or( month == "august" and day <= 22):
	print("Your zodiac sign is Leo")
elif( month == "august" and day >= 23) or( month == "september" and day <= 22):
	print("Your zodiac sign is Virgo")
elif( month == "september" and day >= 23) or( month == "october" and day <= 22):
	print("Your zodiac sign is Libra")
elif( month == "october" and day >= 23) or (month == "november" and day <= 21):
	print("Your zodiac sign is Scorpio")
elif( month = "november" and day >= 22) or (month == "december" and day <= 21):
	print("Your zodiac sign is Sagittarius")
else:
	print("Your zodiac is too far out of my lazy programming.")
