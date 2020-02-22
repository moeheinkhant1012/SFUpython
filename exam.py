x = int(input("Please Enpyter your number: "))
if x == 100:
	print("full mark")
elif x >= 90 and x < 100:
	print("Grade A")
elif x < 90 and x >= 80:
	print("Grade B")
elif x < 80 and x >= 60:
	print("Grade C")
elif x < 60 and x >= 50:
	print("Grade D")
elif x < 50 and x >= 40:
	print("Grade F")
elif x < 40 and x >= 0:
	print("Fail")
else:
	print("check again")
