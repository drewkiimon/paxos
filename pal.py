'''
Proposer, Acceptor, and Learner classes

This document is created in conjunction with
Brett Albano and Chen-Yu Leong to practice and
demonstrate basic knowledge of the consensus
algorithm Paxos.

Written by Andrew Pagan
'''

# A client makes a Node a Proposer
# Proposer has a PID and a value it wants to get passed
class Proposer:
	def __init__(self, pid, value):
		self.p = pid				# In Promise Stage: Higher PID is supreme
		self.v = value				# What it wants

# Majority of nodes/Acceptors need to give OK to Proposer
class Acceptor:
	def __init__(self):
		# Individual list of committed, and not universally shared
		# Individual list of promised, and not universally shared
		self.committed = []				# If it already committed, it's "closed"
		self.promised = []				# Currently engaged in civil union
		self.is_it_committed = False	# Is it too late to promise?

	# During Promise stage
	def promise(self, proposer_pid, proposer_value):
		# Nothing previously promised, so accept it
		if not self.promised:
			self.promised.append(proposer_pid)		#self.promised[0] = pid
			self.promised.append(proposer_value)	#self.promised[1] = value
		elif self.promised and not self.is_it_committed:
		# Checking if we make a new promise
			if proposer_pid > self.promised[0]:		# We make promise to bigger PID
				print("Making a new promise to PID " + str(proposer_pid))
				self.promised[0] = proposer_pid
				self.promised[1] = proposer_value
			else:
				print("Keeping old promise from PID " + str(self.promised[0]))
		elif self.is_it_committed:
			print("It's too late to promise. Already committed.")

	# Committing to promise
	def commit(self):
		if not self.is_it_committed:
			self.is_it_committed = True
			self.committed = self.promised			# Shallow copy should be okay
			print("Congratulations. You've tied the knot.")

# What exactly does the learner do?
class Learner:
	acceptors = []						# Learner knows of all acceptors in the system
	
	def __init__(self):
		self.cool = 'cool'