 import rpyc
from constRPYC import * #-

class Client:
	conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)

	#Looks up the IP address and port number of DBList server:
	(addr, port) = conn_directory.root.exposed_lookup("DBList")
	print (addr, port)

	#Once I have the IP address and port number of app server, just make a connection to it:
	conn = rpyc.connect(addr, port)
	
	#Make RPC calls to app server as usual:
	conn.root.exposed_append(2)
	conn.root.exposed_append(4)
	print (conn.root.exposed_value())