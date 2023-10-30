# Inspiration: 
# https://m.facebook.com/groups/487454506673434/permalink/690030083082541

import random

def month(x):
	if x == 1:
		return "January"
	elif x == 2:
		return "February"
	elif x == 3:
		return "March"
	elif x == 4:
		return "April"
	elif x == 5:
		return "May"
	elif x == 6:
		return "June"
	elif x == 7:
		return "July"
	elif x == 8:
		return "August"
	elif x == 9:
		return "September"
	elif x == 10:
		return "October"
	elif x == 11:
		return "November"
	elif x == 12:
		return "December"

couples = []

# Generate all possible birthday combinations
count = 0
i = 0
for i in range(12):
	for j in range(12-i):
		count = count + 1
		couples.append(month(i+1) + " + " + month(j+i+1))

# Scramble the birthday combinations
scrambled = random.choices(couples, k=len(couples))

# Print the scrambled sequence of birthday combinations
for k in range(len(scrambled)):
	print(k+1, ". ", scrambled[k], sep="")