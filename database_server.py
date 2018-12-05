from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

hostname = "localhost"
port_number = 4000


# handles creation of overall dict and storing key:value in memory
class Database():
	
	def __init__(self):
		self.overall_dict = {}

	def save(self, key, value):
		# add key:value to overall dict (save in memory)
		self.overall_dict[key] = value
		print("OVERALL DICT: ", self.overall_dict)


# handles incoming request from the browser
class RequestHandler(BaseHTTPRequestHandler):
	# handler for GET requests
	def do_GET(self):
		url = urlparse(self.path)
		print("query: ", url) # path='/set', params='', query='somekey=somevalue'
		path = url.path.strip('/')
		query = parse_qs(url.query)

		print("PATH: ", path)
		print("QUERY: ", query)

		if path == "set":
			# method for adding current query dict into overall dict
			self.set_query(query)

		

		# sends a response header and logs the accepted request. HTTP response line sent, followed by Server and Date headers
		self.send_response(200)
		# writes a specific HTTP header to the output stream. keyword:value
		self.send_header("Content-type", "text/plain")
		# sends a black line, indicating the end of the HTTP headers in the response
		self.end_headers()
		self.wfile.write(bytes("HELLO WORLD!", "utf-8"))

	# method for adding current query dict into overall dict
	def set_query(self, dict):
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()

		print("DICT: ", dict) # {'somekey': ['somevalue']}

		for key in dict:
			# store key:value in overall dict
			database.save(bytes(key, "utf-8"), bytes(dict[key][0], "utf-8"))
			print("KEY: ", key)
			print("VALUE: ", dict[key][0])

	

# def run():

database = Database()
# create incoming web server and define the handler to manage the incoming request
server = HTTPServer((hostname, port_number), RequestHandler)
print('Started httpserver on port', port_number)

try:
	# wait forever for incoming http requests
	server.serve_forever()

except KeyboardInterrupt:
	server.server_close()

	


# if __name__ == '__main__':
# 	run()
