# Canadian providences

# Each state is represented by a list with the name and capital in it
# The state name is printed
# The user guesses the captial
# If the capital is in the list then they are correct
# other wise incorrect

yukon = ['Whitehorse']
northwest_territory = ['yellowknife']
nunavut = ["iqaluit"]
british_columbia = ['victoria']
alberta = ['edmonton']
saskatchewan = ['regina']
manitoba = ['winnipeg']
ontario = ['toronto']
quebec = ['quebec city', 'quebec']
newfoundland = ['st. john\'s']
new_brunswick = ['fredericton']
prince_edward = ['charlottetown']
nova_scotia = ['halifax']

global points
points = 0

def yukon_test(yukon, points):
	guess = input("What is the Capital of Yukon? ".capitalize())
	if guess in yukon:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(yukon[0]))

yukon_test(yukon, points)

def northwest_territory_test(northwest_territory, points):
	guess = input("What is the capital of northwest_territory? ".lower())
	if guess in northwest_territory:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(northwest_territory[0]))

northwest_territory_test(northwest_territory, points)

def nunavut_test(nunavut):
	guess = input("What is the capital of nunavut? ".lower())
	if guess in nunavut:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(nunavut[0]))

nunavut_test(nunavut)

def british_columbia_test(yukon, points):
	guess = input("What is the capital of british_columbia? ".lower())
	if guess in british_columbia:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(british_columbia[0]))	

british_columbia_test(british_columbia, points)

def alberta_test(alberta, points):
	guess = input("What is the capital of alberta? ".lower())
	if guess in alberta:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(alberta[0]))

alberta_test(alberta, points)

def saskatchewan_test(saskatchewan):
	guess = input("What is the capital of saskatchewan? ".lower())
	if guess in saskatchewan:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(saskatchewan[0]))

saskatchewan_test(saskatchewan, points)

def manitoba_test(manitoba):
	guess = input("What is the capital of manitoba? ".lower())
	if guess in manitoba:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(manitoba[0]))

manitoba_test(manitoba, points)

def ontario_test(ontario, points):
	guess = input("What is the capital of ontario? ".lower())
	if guess in ontario:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(ontario[0]))	

ontario_test(ontario, points)

def quebec_test(quebec, points):
	guess = input("What is the capital of quebec? ".lower())
	if guess in quebec:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(quebec[0]))

quebec_test(quebec, points)

def newfoundland_test(newfoundland, points):
	guess = input("What is the capital of newfoundland? ".lower())
	if guess in newfoundland:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(newfoundland[0]))

newfoundland_test(newfoundland, points)

def new_brunswick_test(new_brunswick, points):
	guess = input("What is the capital of new_brunswick? ".lower())
	if guess in new_brunswick:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(new_brunswick[0]))

new_brunswick_test(new_brunswick, points)

def prince_edward_test(prince_edward, points):
	guess = input("What is the capital of prince_edward? ".lower())
	if guess in prince_edward:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(prince_edward[0]))

prince_edward_test(prince_edward, points)

def nova_scotia_test(nova_scotia, points):
	guess = input("What is the capital of nova_scotia? ".lower())
	if guess in nova_scotia:
		print('Correct!')
		points += 1
		print('{} / 13'.format(points))
	else:
		print("Incorret. The capital is {}".format(nova_scotia[0]))

nova_scotia_test(nova_scotia, points)

