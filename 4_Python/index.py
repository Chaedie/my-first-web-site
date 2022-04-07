#!C:\Program Files\Python310\python.exe
print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

import cgi, os

files = os.listdir('data')
listStr=''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()
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
    <!-- category -->
    <div id="grid">
        <ol>
            {listStr}
        </ol>
        <!--Main Contents  -->
        <div style id="article">
          <h2>{title}</h2>
          {desc}
          </p>
        </div>
    </div>
</body>
</html>
'''.format(title=pageId,desc=description,listStr=listStr))

print("desc : "+description)
print("pageId :"+pageId)
