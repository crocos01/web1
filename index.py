#!python
print("content-type: text/html; charset=euc-kr\n")
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
print('''<!dotype html>
  <html>
  <head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
  </head>
  <body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
      <li><a href="index.py?id=HTML">HTML</a></li>
      <li><a href="index.py?id=CSS">CSS</a></li>
      <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    </ol>
    <h2>{title}</h2>
    <p>
      월드와이드웹(WorldWideWeb)은 세계 최초의 웹 브라우저이자, 위지윅 HTML 편집 프로그램이다. 1991년 2월 26일에 팀 버너스리가 이 프로그램을 처음 소개하였으며 넥스트스텝 플랫폼 위에서 동작한다. 나중에는 월드 와이드 웹의 이름과 충돌을 피하기 위해 넥서스로 이름이 바뀌었다.
    </p>
  </body>

  </html>
'''.format(title=pageId))
