#!C:\Program Files\Python310\python.exe


import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value
opende_file = open('data/'+title, 'w')
opende_file.write(description)
opende_file.close()

#redirection
print("location: index.py?id="+title)    # HTML is following
print()                                 # blank line, end of headers
