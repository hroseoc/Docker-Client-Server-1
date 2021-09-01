#!/usr/bin/env python3

# Import of python system libraries (these libraries will be used to create the web server)
import http.server
import socketserver 

# This variable handles the requests from client on the server.
handle = http.server.SimpleHTTPRequestHandler

# Here we define that we want to start the server on port 1234. 
# Try to remember this information it will be very useful to us later with docker-compose.
with socketserver.TCPServer(("", 3000), handle) as httpd:
    # This instruction will keep the server running, waiting for requests from the client.
    httpd.serve_forever()

