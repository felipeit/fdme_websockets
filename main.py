from tornado.ioloop import IOLoop
import tornado.httpserver
from tornado.httpserver import HTTPServer
import urls
from tornado.options import parse_command_line
import logging, signal, time, sys


PORT = None

def config():
	parse_command_line()	
	http_server = HTTPServer(urls.ROUTES_TORNADOS)
	port = http_server.listen(PORT)
	signal.signal(signal.SIGINT, lambda sig, frame: shutdown(http_server))
	logging.info('Starting on localhost:{}'.format(PORT))


def shutdown(server):
	ioloop = IOLoop.instance()
	logging.info("Stopping server..")
	server.stop()

	def finalize():
		ioloop.stop()
		logging.info("Stopping..")

	ioloop.add_timeout(time.time() +1.5, finalize)


if __name__ == "__main__":
	PORT = sys.argv[1]
	config()
	IOLoop.instance().start()

