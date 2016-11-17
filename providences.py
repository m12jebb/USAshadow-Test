# Canadian providences

global points
points = 0

# making a dictionary
providences = {
	'Yukon': 'Whitehorse', 
	'Northwest Territory': 'Yellowknife',
	'Nunavut': 'Iqaluit', 
	'British Columbia': 'Victoria', 
	'Alberta': 'Edmonton',
	'Saskatchewan': 'Regina', 
	'Manitoba': 'Winnipeg', 
	'Ontario': 'Toronto',
	'Quebec': 'Quebec City', 
	'Newfoundland': 'St. John\'s', 
	'New Brunswick': 'Fredericton',
	'Prince Edward Island': 'Charlottetown', 
	'Nova Scotia': 'Halifax'
}

def check_dict(providences, points): 
	for key, answer in providences.items():
		guess = input("What is the Capital of {}? ".format(key))
		if guess.upper() == answer.upper():
			print("Correct!")
			points += 1
			print("{} / 13 \n".format(points))
		else:
			print("Incorrect. The Capital is {} \n".format(answer))

print("\nCan you tell me the Capital of each of the Canadian Providences?\n")
check_dict(providences, points)