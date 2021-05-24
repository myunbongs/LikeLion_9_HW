# 가상환경 만들기 python3 -m venv
# 가상환경 실행 source [가상환경명]/bin/activate
# 장고 다운 pip3 install django
# 프로젝트 시작 django-admin startproject[프로젝트이름]
# 서버 기동 python3 manage.py runserver

# MTV 패턴: M(model), T(template), V(view)
# 템플릿: 프론트 앤드(html, css, 템플릿 언어, js)
# 모델: DB
# 뷰: 데이터를 처리하는 곳. MTV의 핵심.

# 장고의 앱은 서비스 별 분류. 하나의 장고 프로젝트를 작게 쪼개는 단위.

# 웹사이트 구동 순서
# 1. 사용자가 서버에 요청
# 2. 서버의 view는 model 에게 요청에 필요한 데이터를 받음
# 3. view는 받은 데이터를 적절하게 처리해서 template으로 넘김
# 4. template은 받은 정보를 사용자에게 보여줌

# 템플릿 언어
# {% for word in wordDic %}
# ...
# {% end %}
#
# {{변수명}}