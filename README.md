# R
# Python

# 스터디계획

0 딥러닝 강의는 맨날 들음

1 서버를 만듦  
2 포브스 또는 유사 신문 사이트를 크롤링하는 방법을 찾음  
3 하루에 한번 자동 크롤링되게 함  

4 분류모델의 input 데이터로 쓰고자 하는 경제 지표를 선정  
5 그 지료를 하루에 한번 저장되게 하는 방법을 찾음  

6-1 하루에 한 번씩 크롤링되는 신문 기사 중 어떻게 한국경제에 영향을 미치는 것을 반영할지 고민  
ex)트럼프(대통령), 전쟁, 정책  
6-2 6으로 해결을 못하면, 공신력 있는 (kbs, ytn)한국 기사를 크롤링하는 것으로 접근  
ex)한국 경제 + 긍부정 형용사 --> 이 것을 분석, 하루에 한 번  

7 rnn, cnn 모델링 실시  
8 맨날 실행되게 함  

9 파이썬 시스템 트레이딩 방법을 공부함  
10 rnn, cnn 모델을 시스템 트레이딩 코드와 연동  
11 자동 거래  


# 리눅스 서버 구축 (2017.03.05 ~) : 삭제하지 말자!  

- 리눅스 설치

1 멀티부팅을 하기 위해서 파티션을 분할한다.(window - minitool partition wizard)  
2 부팅 usb를 만든다(rufus)  
3 바이오스 모드에서 usb 부팅 선택 후 설치를 진행한다.  

4 cent os상의 파티션을 분할한다.(공간확보 후 수동)  
5 네트워크를 설정한다.  
http://www.mizniz.net/31  

6 설치 후 기본설정  
6-1 설치가 완료되면 gui를 설치한다  
sudo yum groups install "GNOME Desktop"  
startx  
6-2 window와 리눅스의 멀티부팅  
6-3 한글 설정 (ibus설치 및 한영키 활성화)  
yum install im-chooser  
im-chooser #ibus 선택   
vi /usr/share/X11/xkb/symbols/altwin # melt_alt의 symbols[Group]을 Hangul로 변경  


- 서버 구축

7 bitnami 설치 : run파일 => chmod a+x 프로그램 => ./프로그램  
8 마리아디비 설정  
9 방화벽 설정  

- 깃 구축

10 깃 설치 및 ssh파일 받기  
https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/   
11 홈페이지에 등록  
12 클론 및 풀  
13 아톰 에디터 설치(필요한 패키지 : git-puls, autocomplete-python, python-indent)  

- 크롤링

14 python3 설치 및 필요모듈 다운로드  
15 git 연동  

- 도움이 되는 사이트  

가비아 라이브러리
https://tecadmin.net/   
생활코딩(도메인) https://opentutorials.org/course/228/1450    
인프런 이것이 리눅스다 https://www.inflearn.com/course/%ec%9d%b4%ea%b2%83%ec%9d%b4-%eb%a6%ac%eb%88%85%ec%8a%a4%eb%8b%a4/    


---------------
# 그 밖의 접속      
접속 시 중요한 것은, 서버에서는 방화벽 허용 및 포트 포워딩해야 하며 클라이언트는 전용 툴이 있어야 한다.  

1. 웹 접속(80) : bitnami lamp(리눅스) 및 도메인 활용     

2. telnet접속(23) : telnet 서버아이피(윈도우, 맥 동일)   
서버는 서버 및 클라이언트 설치, 클라이언트는 설치해야 한다.(root이외의 별도의 계정을 만들어야 함)   
윈도우는 활성화만 하면 되지만, 맥은 brew로 설치해야 한다.

3. ssh접속(22) : ssh 서버계정아이디@서버아이피(윈도우, 맥 동일)   
서버는 openssh가 설치해야 하나, 센토스에서는 기본으로 셋팅해줌.    
윈도우의 경우 putty를 설치하면 커맨드에서도 활용가능, 맥은 그대로 활용해도 된다.(root이외의 별도의 계정을 만들어야 함)  
(telnet과 ssh는 텍스트기능만 제공한다.)  

4. 데이터접속(3306) : 앞의 경우와 다르게, 접속자에게 권한을 줄 수 있도록 쿼리문을 실행해야 한다.
use mysql;  
Grant All PRIVILEGES ON *.* TO '아이디'@'%(아이피)' IDENTIFIED BY '비밀번호';  
MySQL : bitnami lamp를 활용해서 phpmyadmin으로 접속하면 된다.  
MariaDB : GUI툴로 윈도우의 경우 HeidiSQL, 맥은 Sequel Pro가 있다.


-------

# 우분투 설치  

playonlinux로 카카오톡을 설치한다  
git : ssh 연결  

apt-get : 설치  
su root : root권한 얻기  
