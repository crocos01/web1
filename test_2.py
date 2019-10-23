#!python
print("content-type: text/html; charset=euc-kr\n")
import cgi
form = cgi.FieldStorage(keep_blank_values=True)
for name in form.keys():
    list = "input:"+name+" value:"+form[name].value
    print(list)
try:
    pageId = form["id"].values
except(KeyError, TypeError):
    pageId = 'a'
print(3)
print(pageId)
