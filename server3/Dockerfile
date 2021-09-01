FROM python:latest
# 'server.py' is the name of the file on the host.
# '/server/' is the path where to put the file on the image.
# Putting files at the image '/server/' folder.
ADD server3.py /server3/
ADD index.html /server3/
# Define '/server/' as base directory (where all commands will be executed).
WORKDIR /server3/