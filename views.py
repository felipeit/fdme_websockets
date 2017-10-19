from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler
import re
import redis


class ConnectWithRedis:
	def __init__(self, nome):
		self.nome = nome
		self.response = redis.ConnectionPool(host='localhost', port=6379, db=0)
		super().__init__()

	def redis_set(self):
		client = redis.Redis(connection_pool=self.response)
		response = client.get(self.nome)
		return response


class MainSocket(WebSocketHandler):	
	def open(self):
		print("Opening connecton..")

	def on_message(self, message):
		localization = message.split('\n')	
		if len(localization) > 3: 
			longitude = re.findall('[-,'']\d+\.\d+', localization[2])
			latitude = re.findall('[-,'']\d+\.\d+', localization[3])
			username = localization[-1] 
			value = {
				"longitude": longitude,
			 	"latitude": latitude
			 }
			client = ConnectWithRedis(username)
			client.set(username, value)
		else:
			print("Localization not found")		

	def on_close(self):
		print("Closing connection..")

		
class MainWeb(RequestHandler):
 
    def get(self):
        self.write("Hello friend.")
