import socket, OSC, re, time, threading, math
import event


class PiException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)


class OscReceive :

	def __init__(self, port):
		self.receive_address = '0.0.0.0', port #Mac Adress, Outgoing Port
		self.s = OSC.OSCServer(self.receive_address)
		self.s.addDefaultHandlers()
		self.setup("/test")
		# Start OSCServer
		print "\nStarting OSCServer. Use ctrl-C to quit."
		self.st = threading.Thread( target = self.s.serve_forever )
		self.st.start()


 	def setup(self, adr):
		self.s.addMsgHandler(adr, self.callback)
		print "Registered Callback-functions are :"
		for addr in self.s.getOSCAddressSpace():
			print addr

 	def callback(self, add, tags, stuff, source):
		print add
		event.bang(add, stuff)

	def terminate(self):
		print "\nClosing OSCServer."
		self.s.close()
		print "Waiting for Server-thread to finish"
		self.st.join()
		print "Done"



# ADD callbacl function with event.py as follows,
# import event
# def foo(vals):
#   for val in vals:
#     print val
# event.add("foo",foo)
