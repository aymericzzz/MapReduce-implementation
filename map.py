# -*-coding:Latin-1 -*

#map function
def map_function(input):
	#declaration of a list to store our (key,value) pairs
	list = []
	i = 0
	#reading of every cell of the input parameter
	for line in input:
		#adding of a list to the list for this line/iteration
		list.append([])
		#splitting of every word
		words_array = line.split()
		#reading of every word
		for word in words_array:
			#add every word as a (key, value) pair
			list[i].append((word, 1))
		i+=1
	return list