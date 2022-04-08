#!C:\Program Files\Python310\python.exe
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

import cgi, os
import view

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
    # dsecription = description.replace('<','&lt;')
    # dsecription = description.replace('>','&gt;')
    description= sanitizer.sanitize(description)
else:
    pageId = "Welcome"
    description = "Hello, web"
#Description of the Webpage
print('''<!doctype html>
<html>
<head>
    <title>Hello Web!</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.py">Hello Web!!!</a></h1>
    <ol>
        {listStr}
    </ol>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
        <p><input type="submit"></p>
    </form>
</body>
</html>
'''.format(
    title=pageId,
    desc=description,
    listStr=view.getList()))

print("desc : "+description)
print("pageId :"+pageId)
