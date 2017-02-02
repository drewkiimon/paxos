'''
This Paxos conesus algorithm demonstrates basic knowledge
and thought process behind the steps. 

Written by Andrew Pagan
'''

from pal import *

import paxos_func
import random
import time

#time.sleep(MINUTE)
SECOND = 1
MINUTE = 60	* SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

NODE_TYPE = ('Proposer', 'Acceptor', 'Learner')
ACCEPTORS = []
def paxos():
	# Random amount of nodes (Acceptor + Proposer + Learner)
	number_of_nodes = random.randint(3, 10)
	
	# Initialize all roles
	number_of_acceptors = number_of_nodes - 2		#Learner and Proposer
	paxos_func.add_acceptors(number_of_acceptors, ACCEPTORS)
	
	p, v = input('Enter proposed PID, Value: ')
	
	d_proposer = Proposer(p, v)		# Distinguished Proposer
	d_acceptor = Learner()			# Distinguished Learner
	
	#PROMISE phase
	

	#COMMIT phase