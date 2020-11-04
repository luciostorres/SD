import rpyc
import socket
from constRPYC import * #-
from rpyc.utils.server import ForkingServer

class DBList(rpyc.Service):
	value = []

	def exposed_append(self, data):
		self.value = self.value + [data]
		print ("Appended value: ", data)
		return self.value

	def exposed_value(self):
		return self.value

if __name__ == "__main__":
	server = ForkingServer(DBList, port = 12346)

	conn = rpyc.connect(DIR_SERVER, DIR_PORT)

	my_addr = socket.gethostbyname(socket.gethostbyname())

	print (conn.root.exposed_register("DBList", my_addr, 12346))
	server.start()