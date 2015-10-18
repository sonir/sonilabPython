import socket, OSC, re, time, threading, math


class PiException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)


class SlOscReceive :

	def __init__(self, port, object):
	#		self.receive_address = '127.0.0.1', 7000 #Mac Adress, Outgoing Port
		self.receive_address = '0.0.0.0', port #Mac Adress, Outgoing Port
		self.s = OSC.OSCServer(self.receive_address)
		self.s.addDefaultHandlers()
		self.obj = object

		self.setup()
		# just checking which handlers we have added
		print "Registered Callback-functions are :"
		for addr in self.s.getOSCAddressSpace():
			print addr

		# Start OSCServer
		print "\nStarting OSCServer. Use ctrl-C to quit."
		self.st = threading.Thread( target = self.s.serve_forever )
		self.st.start()


	def setup(self):
		self.s.addMsgHandler("/test1", self.test1)
		self.s.addMsgHandler("/test2", self.test2)


	def test1(self, add, tags, stuff, source):
		print("test1")
		self.obj.callback("/test1",1,2.2)

	def test2(self, add, tags, stuff, source):
		print "X Value is: "
		print stuff[0]
		print "Y Value is: "
		print stuff[1]  #stuff is a 'list' variable
		self.obj.callback("/test2", 2, 3.3)

	def update(self):
		pass

	def terminate(self):
		print "\nClosing OSCServer."
		self.s.close()
		print "Waiting for Server-thread to finish"
		self.st.join()
		print "Done"
