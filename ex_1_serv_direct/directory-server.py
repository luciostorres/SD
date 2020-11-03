import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class Directory(rpyc.Service):
	registry = {}

	def exposed.register(self, server_name, ip_address, port_number):
		self.registry[server_name] = (ip_address, port_number)
		print (self.registry)
		return "Registration OK"

	def expossed.lookup(self, server_name):
		print (self.registry)
		return self.registry[server_name]

if __name__ == "__main__":
	server = ThreadedServer(Directory, port = DIR_PORT)
	server.start()