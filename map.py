# -*-coding:Latin-1 -*

#map function
def map(input):
	#declaration of a list to store our (key,value) pairs
	#dict = {}
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
			# check if the word is in the dictionnary. If yes, increase the key value. If not, declare the word as a key and with a value of 1.
			#if word in dict.keys():
				#dict[word] += 1
			#else: 
				#dict[word] = 1
		#list_line1 = [(a, b) for a, b in dict.items()]
			list[i].append((word, 1))
	i+=1