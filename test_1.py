#!python
print("content-type: text/html; charset=euc-kr\n")
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
pageId = form["id"].value
print('''
<!dotype html>
<html>
<head>
<title>test_1</title>
</head>
<body>
<h1>test_1</h1>
</body>
</html>
''')
