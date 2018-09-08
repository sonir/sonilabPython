from collections import deque
import event


class EventCue:

	def __init__(self):
		self.deq = deque()

	def add(self,adr, *args):
		self.deq.append((adr, args))

	def dump(self):
		for elm in self.deq:
			event.bang(elm[0],*elm[1])
			# print elm[0]
			# for elm2 in elm[1]:
			# 	print "arg:", elm2
