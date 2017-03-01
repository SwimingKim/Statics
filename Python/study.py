identity = '지구인'
number_of_legs = 4
print('안녕! 나는', identity, '이야, 나는 다리가', number_of_legs, '개 있어')

identity = '한국인'
number_of_legs = 2
print('안녕! 나는', identity, '이야, 나는 다리가', number_of_legs, '개 있어')

# 한줄 주석
"""
여러줄 주석
"""

# 숫자 - 수학 연산이 가능
# 문자열 - 화면에 그대로 출력 가능, 따옴표로 둘러싸서 표시
multiply = 9*9
divide = 30/5
power = 2**10
reminder = 15%4
print(multiply, divide, power, reminder)

# REPL(Read Eval Print Loop)
# python3 <-> exit()

# shell
# pwd : 현재 폴더 경로 출력
# ls : 현재 폴더 내용물 출력
# cd : 다른 폴더로 이동
# cp : 파일을 다른 이름으로 복사
# rm : 파일을 삭제

people = 3
apple = 20

if people < apple / 5:
    print('신나는 사과 파티! 배 터지게 먹자!')

# 조건
# 숫자 비교 : < > <= >= == !=
# boolean 연산 : and or not

if True:
    print('블록에 속한 코드')
    if False:
        print('또 한 줄 더')
    print('블럭의 끝 코드')
print('블럭 끝')

# if, else, elis
SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼다'
DRAW = '비겼다'
LOSE = '졌다'

mine = '가위'
yours = '바위'

if mine == yours:
    result = DRAW
else:
    if mine == SCISSOR:
        if yours == ROCK:
            result = LOSE
        else:
            result = WIN
    elif mine == PAPER:
        if yours == SCISSOR:
            result = LOSE
        else:
            result = WIN
    else:
        print('이상해요')
print (result)

# 함수
def function():
    print('안녕 함수!') # 내장 함수
function() # 직접 만든 함수

# 매개변수 : 정의에서 사용하는 이름
# 실행인자 : 실행할 때 넘기는 값
def print_sqrt(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print('해는 {} 또는 {}'.format(r1, r2))
print_sqrt(2, -6, -8)

def print_round(number):
    rounded = round(number)
    print(rounded)
print_round(4.6)

# 함수의 return
def add_10(value):
    """value에 10을 더한 값을 돌려주는 함수"""
    if value < 10 :
        return 10
    result = value + 10
    return result
n = add_10(42)
print(n)
n = add_10(5)
print(n)

def root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2
r1, r2 = root(2, -6, -8)
print('근은 {} {}'.format(r1, r2))

# format
number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'

print(number, '번 손님', greeting, '.', place, '에 오신 것을 ', welcome, '!')
base = '{}번 손님, {}. {}에 오신 것을 {}!'
new_way = base.format(number, greeting, place, welcome);
print(base)
print(new_way)
print('나는 {}, 너는 {}, 그래서 {}'.format(yours, mine, result))

# 문자열
string1 = 'Some text'
string2 = "어떤 텍스트"
string3 = '{}도 {}도 지금 이것도 문자열'.format(string1, string2)
print(string3)

quote = '따옴표로 싼 문자열 안에는 큰따옴표(")를 사용할 수 있다.'
emphasize = "큰따옴표로 싼 문자열 안에는 따옴표(')를 사용할 수 있다."
long_string = '''첫째줄은 좋은데
둘째줄도 괜찮을까?'''
print(long_string)
quote1 = "가끔은 '와" + '"를 모두 쓰기도 해'
quote2 = """가끔은 '와 "를 모두 쓰기도 해"""
print(quote1)
print(quote2)

# 정수와 실수
five1 = 5
five2 = 5.0
five3 = 5.00000
print(five1)
print(five2)
print(five3)
five4 = 5 * 1
five5 = 5 * 1.0
print(five4)
print(five5)
div1 = 6 / 5 # 1.2
div2 = 6 // 5 # 1
print(div1)
print(div2)
a = 6
b = 5
print(a == b * (a // b) + (a % b))
print(int(5.0))
print(float(5))

# 사용자 입력 받기 : input
# ctrl + c 프로그램 즉시 종료 가능
"""
print('가위 바위 보 가운데 하나를 내주세요>', end = ' ')
mine = input()
mine = input('가위 바위 보 가운데 하나를 내주세요>')
print('mine:', mine)
"""

# 리스트
list1 = ['가위', '바위', '보']
list2 = [37, 23, 10, 33, 29, 40]
print(list1)
print(list2[0])
print(list2[-1])
# 추가방법
list2.append(16)
list3 = list2 + [16]
list4 = list2 + list3
# 값 존재 확인
n = 12
ownership = n in list3
print(ownership)
n = 10
if n in list3:
    print('{}은 있어!'.format(n))
# 삭제방법
del(list4[12])
list4.remove(16) # 해당 값
print(list4)
list4.pop(0) # 인덱스

# for문
# for in list : 순회할 리스트가 정해져 있을 때
for row in list1:
    print(row)
# for in range() : 순회활 횟수가 정해져 있을 때
for i in range(10):
    print(i)
names = ['철수', '영희', '바둑이', '귀도']
for i in range(len(names)):
    name = names[i]
    print('{}번: {}'.format(i+1, name))
# for index, row in enumerater()
for i, name in enumerate(names):
    print('{}번: {}'.format(i+1, name))
# for i in range(11172):
    # print(chr(44032+i), end='')

# 모듈 사용하기
def get_web(url):
    """URL을 넣으면 페이지 내용을 돌려주는 함수"""
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded
"""
url = input('웹 페이지 주소? ')
content = get_web(url)
print(content)
"""
import mymodule # 같은 폴더!
selected = mymodule.random_rsp()
print(selected);
print('가위? ', mymodule.SCISSOR == selected)

# 딕션너리
wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
}
print(wintable['가위'])
def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'
message = {
    'win' : '이겼다!',
    'draw' : '비겼네.',
    'lose' : '졌어'
}
result = rsp('가위', '바위')
print(message[result])
# 딕션너리 값 변경
dict = {
    'one':1,
    'two':2
}
dict['one'] = 11 # 수정
dict['three'] = 3 # 추가
del(dict['one']) # 삭제1
dict.pop('two') # 삭제2
# 딕셔너리 반복문
seasons = ['봄', '여름', '가을', '겨울']
for row in seasons:
    print(row)
ages = {'Tod':35, 'Jane':23, 'Paul':62}
"""
for key in ages.keys():
    print(key);
for value in ages.values():
    print(value);
for key in ages: # for key in ages.keys():
    print('{}의 나이는 {}입니다'.format(key, ages[key]))
"""
for key, value in ages.items():
    print('{}의 나이는 {}입니다'.format(key, value))
ages.clear() # 전부 삭제
dict1 = {1:100, 2:200}
dict2 = {1:1000, 3:300}
dict2.update(dict1)
print(dict2)

# 튜플
# 순서를 바꾸거나 값을 변경할 수 없다
tuple1 = (1, 2, 3)
typle2 = 1,2,3
tuple3 = tuple(list1)
print(tuple1[0])
# packing, unpacking
c = (3, 4) # packing
d, e = c # unpacking
f = d, e # packing
a, b = 1, 2
a, b = b, a

list = [1,2,3,4,5]
# for a in enumerate(list):
    # print ('{}번째 값: {}'.format(a[0], a[1]))
for a in enumerate(list):
    print ('{}번째 값: {}'.format(*a))
ages = {'Tod':35, 'Jane':23, 'Paul':62}
# for a in ages.items():
    # print('{}의 나이는 : {}'.format(a[0], a[1]))
for a in ages.items():
    print('{}의 나이는 : {}'.format(*a))
