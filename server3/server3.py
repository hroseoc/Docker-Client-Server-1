#!/usr/bin/env python3

# Imports the python system library.
import urllib.request

# Import of python system libraries (these libraries will be used to create the web server)
import http.server
import socketserver 

# This variable handles the requests from client on the server.
handle = http.server.SimpleHTTPRequestHandler

# Here we define that we want to start the server on port 1234. 
# Try to remember this information it will be very useful to us later with docker-compose.
with socketserver.TCPServer(("", 4000), handle) as httpd:
    # This instruction will keep the server running, waiting for requests from the client.
    httpd.serve_forever()

# The req variable contains the request on 'http://localhost:4000/'.
req = urllib.request.urlopen("http://localhost:4000/")

# 'encodedContent' correspond to the server response encoded ('index.html').
# 'decodedContent' correspond to the server response decoded (i.e., what we want to display).
encodedContent = req.read()
decodedContent = encodedContent.decode("utf8")

# Display the server file: 'index.html'.
print(decodedContent)

# Close the server connection.
req.close()

