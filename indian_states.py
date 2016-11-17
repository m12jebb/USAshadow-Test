# Indian States

global points
points = 0

# making a dictionary
providences = {
	'Andhra Pradesh': 'Whitehorse', 
	'Arunachal Pradesh': 'Yellowknife',
	'Assam': 'Iqaluit', 
	'Bihar': 'Victoria', 
	'Chandigarh': 'Edmonton',
	'Chhattisgarh': 'Regina', 
	'Goa': 'Winnipeg', 
	'Gujarat': 'Toronto',
	'Haryana': 'Quebec City', 
	'Himachal Pradesh': 'St. John\'s', 
	'Jammu and Kashmir': 'Fredericton',
	'Jharkhand': 'Charlottetown', 
	'Karnataka': 'Halifax',
	'Kerala': 'Halifax',
	'Lakshadweep': 'Halifax',
	'Madhya Pradesh': 'Halifax',
	'Karnataka': 'Halifax',
	'Maharashtra':
	'Manipur':
	'Meghalaya':
	'Mizoram':
	'Nagaland':
	'Odisha':
	'Puducherry':
	'Punjab':
	'Rajasthan':
	'Sikkim':
	'Tamil Nadu':
	'Telangana':
	'Tripura':
	'Uttar Pradesh':
	'Uttarakhand':
	'West Bengal':
}

def check_dict(providences, points): 
	for key, answer in providences.items():
		guess = input("What is the Capital of {}? ".format(key))
		guess = guess.title()
		if guess == answer:
			print("Correct!")
			points += 1
			print("{} / 13 \n".format(points))
		else:
			print("Incorrect. The Capital is {} \n".format(answer))

print("\nCan you tell me the Capital of each of the Canadian Providences?\n")
check_dict(providences, points)