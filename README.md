# R
# Python

# 스터디계획
>
0 딥러닝 강의는 맨날 들음
>
1 서버를 만듦\n
2 포브스 또는 유사 신문 사이트를 크롤링하는 방법을 찾음\n
3 하루에 한번 자동 크롤링되게 함
>
4 분류모델의 input 데이터로 쓰고자 하는 경제 지표를 선정
5 그 지료를 하루에 한번 저장되게 하는 방법을 찾음
>
6-1 하루에 한 번씩 크롤링되는 신문 기사 중 어떻게 한국경제에 영향을 미치는 것을 반영할지 고민
ex)트럼프(대통령), 전쟁, 정책
6-2 6으로 해결을 못하면, 공신력 있는 (kbs, ytn)한국 기사를 크롤링하는 것으로 접근
ex)한국 경제 + 긍부정 형용사 --> 이 것을 분석, 하루에 한 번
>
7 rnn, cnn 모델링 실시
8 맨날 실행되게 함
>
9 파이썬 시스템 트레이딩 방법을 공부함
10 rnn, cnn 모델을 시스템 트레이딩 코드와 연동
11 자동 거래


# 리눅스 서버 구축 (2017.03.05 ~)

- 리눅스 설치 (~03.06)
>
1 멀티부팅을 하기 위해서 파티션을 분할한다.(window - minitool partition wizard)
2 부팅 usb를 만든다(rufus)
3 바이오스 모드에서 usb 부팅 선택 후 설치를 진행한다.
>
4 cent os상의 파티션을 분할한다.(공간확보 후 수동)
5 네트워크를 설정한다.
http://www.mizniz.net/31
>
6 설치 후 기본설정
6-1 설치가 완료되면 gui를 설치한다
sudo yum groups install "GNOME Desktop"
startx
6-2 window와 리눅스의 멀티부팅
6-3 한글 설정 (ibox설치 및 한영키 활성화)

- 서버 구축 (~03.09)
>
7 mariadb mariadb-server를 설치한다.
8 방화벽 설정 및 iptables
9 아이피 고정

- 크롤링
>
10 python3 설치 및 필요모듈 다운로드
11 git 연동
