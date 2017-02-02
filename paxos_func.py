from pal import *

def add_acceptors(number_of_acceptors, list_of_acceptors):
	iter = 0
	while iter < number_of_acceptors:
		list_of_acceptors.append(Acceptor())
		iter = iter + 1
	print (len(list_of_acceptors))
	return list_of_acceptors