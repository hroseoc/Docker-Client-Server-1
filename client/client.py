#!/usr/bin/env python3

# Imports the python system library.
import urllib.request

# The req variable contains the request on 'http://localhost:3000/'.
req = urllib.request.urlopen("http://localhost:3000/")

# 'encodedContent' correspond to the server response encoded ('index.html').
# 'decodedContent' correspond to the server response decoded (i.e., what we want to display).
encodedContent = req.read()
decodedContent = encodedContent.decode("utf8")

# Display the server file: 'index.html'.
print(decodedContent)

# Close the server connection.
req.close()