# -*-coding:Latin-1 -*

def reduce_function(input):
	for key, value in input.items():
		if type(value) != int:
			input[key] = sum(value)
	return input