# -*-coding:Latin-1 -*

def reduce_function(input):
	# read every pair 
	for key, value in input.items():
		# if the value is not a single int
		if type(value) != int:
			# then we sum all the values => reduce
			input[key] = sum(value)
	return input