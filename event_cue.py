from collections import deque
import event


class EventCue:

	def __init__(self):
		self.deq = deque()

	def add(self,adr, *args):
		self.deq.append([adr, args])

	def dump(self):
		while len(self.deq):
			elm = self.deq.popleft()
			event.bang(elm[0],*elm[1])
