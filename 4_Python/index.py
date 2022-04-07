#!C:\Program Files\Python310\python.exe

print("Content-Type: text/html")    # HTML is following
print()                             # blank line, end of headers

print("It's hard to start python coding")

print('''<!doctype html>
<html>
<head>
  <title>Hello Web!</title>
  <meta charset="utf-8">
</head>

<body>
  <h1><a href="index.html">Hello Web!!!</a></h1>
  <!-- category -->
  <div id="grid">
    <ol>
      <li><a href="1.html">Why not VN?</a></li>
      <li><a href="2.html">What's Next?</a></li>
      <li><a href="3.html">And then?</a></li>
    </ol>
    <!--Main Contents  -->
    <div style id="article">
      <h2>개발자가 되는 이야기</h2>
      안녕하세요, 임채동입니다.<br>
      제가 처음으로 만든 웹사이트에 오신걸 환영합니다.<br><br>
      여기선 제가 왜 개발자의 길을 걷게 되었는지, <br>
      그리고 어떤 경로로 개발자가 되어가고 있는지<br>
      블로그 형식으로 단계별로 알수있는 사이트입니다.<br>
      별것 없는 사이트지만 개발이라는 분야에 입문하여<br>
      처음으로 만드는 역사적인 사이트이니 재밌게 봐주세요 ^^<br><br>

      <p>
      <h2>기획안</h2>
      <img src="기획안.jpg" width="80%">
      <br><br>
      최초 기획안은 위와 같습니다.<br>
      1번부터 시작하여 어떤 생각으로 커리어 전환을 계획하게 되었는지<br>
      어떤 과정을 통해 공부할 계획인지 등에 대해<br>
      개략적으로 적어보도록 하겠습니다.<br>
      </p>
    </div>
  </div>
</body>
</html>

''')