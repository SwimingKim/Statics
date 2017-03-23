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

list1 = [1,2,3,4,5]
# for a in enumerate(list):
# print ('{}번째 값: {}'.format(a[0], a[1]))
for a in enumerate(list1):
    print ('{}번째 값: {}'.format(*a))
ages = {'Tod':35, 'Jane':23, 'Paul':62}
# for a in ages.items():
# print('{}의 나이는 : {}'.format(a[0], a[1]))
for a in ages.items():
    print('{}의 나이는 : {}'.format(*a))

# while문
selected = None
# while selected not in ['가위', '바위', '보']:
# selected = input('가위, 바위, 보 중에 선택하세요>')
# print('선택된 값: ',selected)

patterns = ['가위', '바위', '보']
# for pattern in patterns:
# print(pattern)
# for i in range(len(patterns)):
# print(patterns[i])
length = len(patterns)
i = 0
while i < length:
    print(patterns[i])
    i += 1

# break, continue
list1 = [1,2,3,5,7,2,5,237,55]
for val in list1:
    if val % 3 == 0:
        print(val)
        break
# for i in range(10):
#     if i%2 != 0:
#         print(i)
#         print(i)
#         print(i)
#         print(i)
for i in range(10):
    if i%2 == 0:
        continue
    print(i)
    print(i)
    print(i)
    print(i)

# try except
text = "100%"
try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아니네요'.format(text))

def safe_pop_print(mylist, index):
    # try:
    #     print(list.pop(index))
    # except IndexError:
    #     print('{} index의 값을 가져올 수 없습니다'.format(index))
    if index<len(mylist):
        print(mylist.pop(index))
    else:
        print('{} index의 값을 가져올 수 없습니다'.format(index))
safe_pop_print([1,2,3],5)
try:
    import module
except ImportError:
    print('모듈이 없습니다')

# 예외 이름을 모르는 경우
try:
    mylist = []
    # print(list[0])
    text = 'abc'
    number = int(text)
except Exception as ex:
    print('{} 에러가 발생했습니다.'.format(ex))

# raise
def rsp(mine, yours):
    allowed = ['가위','바위','보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError
try:
    rsp('가위', '바')
except ValueError:
    print('잘못된 값을 넣은 것 같습니다')

school = {'1반':{172,185,198,177,165,199}, '2반':{165,177,167,180,191}}
try:
    for class_number, students in school.items():
        for student in students:
            if student>190:
                print(class_number,'반에 190을 넘는 학생이 있습니다')
                raise StopIteration
                # break
except StopIteration:
    print('정상종료')

# 논리연산
a = 10
if a<0 and 2**a>1000 and a%5==2 and round(a)==a:
    print('복잡한 식')
def return_false():
    print('함수return_false')
    return False
def return_true():
    print('함수return_true')
    return True
print('테스트1')
a = return_false()
b = return_true()
if a and b:
    print(True)
else:
    print(False)
print('테스트2')
if return_false() and return_true():
    print("True")
else:
    print(False)

dic = {"Key2":"Value1"}
if "Key1" in dic and dic["Key1"] == "Value":
    print("Key1도 있고, 그 값은 Value1이네")
else:
    print("아니네")

# bool과 논리연산
# 숫자 0을 제외한 모든 수 - true
# 빈 딕셔너리, 빈 리스트를 제외한 모든 딕셔너리, 리스트 - true
# 아무 값도 없다는 의미인 None - false
# 빈문자열을 제외한 모든 문자열 - true
# value = input('입력해주세요>') or '아무것도 못받았어'
# print('입력받은 값>', value)

# list의 기능
list1 = [135, 467, 27, 2754, 234]
list1.index(27)
list2 = [1,2,3] + [4,5,6]
list1.extend([9,10,11])
list1.insert(2, 999)
list1.sort() # 정렬
list1.reverse() # 거꾸로

# list와 String
print(27 in list1)
str = "HelloWorld"
print("H" in str)
str.index("r")
charaters = list('abcdef')
print(charaters)
words = "Hello wolrd는 프로그래밍을 배우기에 아주 좋은 사이트"
words_list = words.split() # string to list
print(words_list)
new_words = " ".join(words_list) # list to string
print(new_words)

# slicing
text = "hello world"
print(text[1:5])
list1 = ['영','일','이','삼','사','오']
print(list1[1:3])
print(list1[0:2])
print(list1[2:len(list1)])

# step
# list1 = [1,2,3,4,5,6,7,8,9,10]
list1 = list( range(10) )
print(list1[1:10:2])
print(list1[10:2:-1])

numbers = [0,1,2,3,4,5,6,7,8,9]
del numbers[0]
print(numbers)
del numbers[ :5]
print(numbers)
numbers[1:3] = [77,88]
print(numbers)

# 자료형
s = "Hello world"
print( type(s) )
i = 42
print( type(i) )
print(isinstance(42, int))

# 클래스와 인스턴스
numbers1 = []
print(type(numbers))
print(numbers1 == list)

# 클래스
class Human():
    '''사람'''
person1 = Human()
person2 = Human()
print(isinstance(person1, Human))
person1.language = '한국어'
person2.language = 'English'
print(person1.language)
print(person2.language)

def speak(person) :
    print("{}로 말을 합니다".format(person.language))
Human.speak = speak
person1.speak() # speak(person1)
person2.speak() # speak(person2)

# 모델링
def create_human(name, weight) :
    person = Human()
    person.name = name
    person.weight = weight
    return person
Human.create = create_human
person = Human.create("철수",60.5)
def eat(person) :
    person.weight += 0.1
    print("{}가 먹어서 {}kg이 되었습니다".format(person.name, person.weight))
def walk(person) :
    person.weight -= 0.1
    print("{}가 걸어서 {}kg이 되었습니다".format(person.name, person.weight))
Human.eat = eat
Human.walk = walk

person.walk()
person.eat()
person.walk()

# 메소드
class Human():
    '''인간'''
    def create(name, weight) :
        person = Human()
        person.name = name
        person.weight = weight
        return person
    def eat(self) :
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))
    def walk(self) :
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))
    def speak(self, message) :
        print(message)
person = Human.create("철수",60.5)
person.walk()
person.eat()
person.walk()
person.speak("안녕하세요")

# 초기화 / 문자열화 함수
class Human():
    '''인간'''
    def __init__(self, name, weight) :
        '''초기화 함수'''
        # print("__init__실행")
        self.name = name
        self.weight = weight
        # print("이름은 {}, 몸무게는 {}".format(name, weight))
    def __str__(self) :
        '''문자열화 함수'''
        return "{}(몸무게 {}kg)".format(self.name, self.weight)
person = Human("사람", 60.5)
print(person.name)
print(person)

# 상속
class Animal():
    def walk(self):
        print("걷는다")
    def eat(self) :
        print("먹는다")

class Human(Animal) :
    def wave(self) :
        print("손을 흔든다")
class Dog(Animal) :
    def wag(self) :
        print("꼬리를 흔든다")
person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()

# 오버라이드 & super()
class Animal():
    def __init__(self, name):
        self.name = name
    def walk(self):
        print("걷는다")
    def eat(self) :
        print("먹는다")
    def greet(self) :
        print("{}이/가 인사한다".format(self.name))
class Cow(Animal) :
    '''소'''

class Human(Animal) :
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand
    def wave(self) :
        print("{}을 흔들면서".format(self.hand))
    def greet(self) :
        self.wave()
        super().greet()

class Dog(Animal) :
    def wag(self) :
        print("꼬리를 흔든다")
    def greet(self) :
        self.wag()

person = Human("사람", "오른손")
person.greet()
# dog = Dog()
# dog.greet()
# cow = Cow()
# cow.greet()

# 예외 정의
class UnexpectedRSPValue(Exception):
    '''가위 바위 보 중에 하나가 아닌 경우의 에러'''

value = '가'
try:
    if value not in ['가위','바위','보']:
        # raise ValueError("가위바위보 중에 하나의 값이어야 합니다")
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print("에러가 발생했습니다")

def sing_up():
    '''회원가입 함수'''

try:
    sing_up()
except BadUserName:
    print("이름으로 사용할 수 없는 입력입니다")
except PasswordNotMatched:
    print("입력한 패스워드가 불일치합니다")

# List Comprehension
# 예1 [ i*i for i in range(1,11) ] # [ 계산식 for문 ]
# 예2 [ i*i for i in range(1,11) if i % 2 == 0 ] # [ 계산식 for문 조건문 ]
# 예3 [ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]
areas = []
for i in range(1,11):
    if i%2==0:
        areas = areas + [i*i]
print(areas)
areas2 = [i*i for i in range(1,11)]
print("areas2 : ", areas2)
areas3 = [i*i for i in range(1,11) if i%2 ==0]
print("areas3 : ", areas3)
print([(x,y) for x in range(15) for y in range(15)])

# Dictionary Comprehension
students = ["태연", "진우", "정현", "하늘", "성진"]
for number, name in enumerate(students):
    print("{}번의 이름은 {}입니다".format(number, name))
student_dict = { "{}번".format(number+1) : name for number, name in enumerate(students) }
print(student_dict)

scores = [85, 92, 78, 90, 100]
for x,y in zip(students, scores):
    print(x,y)
scroe_dict = {student:score for student,score in zip(students, scores)}
print(scroe_dict)

# datetime모듈
import datetime
print(datetime.datetime.now())
start_time = datetime.datetime.now()
print(type(start_time))
start_time = start_time.replace(year=2016, month=2, day=1)
print(start_time)
start_time = datetime.datetime(2018,2,1)
print(start_time)
how_long = start_time - datetime.datetime.now()
print(type(how_long))
print(how_long.days)

# timedelta 클래스
hundred = datetime.timedelta(days=100)
print(datetime.datetime.now()+hundred)
hundred_before = datetime.timedelta(days=-100)
print(datetime.datetime.now()+hundred_before)
print(datetime.datetime.now()-hundred)

tommorrow = datetime.datetime.now().replace(hour=9, minute=0, second=0) + datetime.timedelta(days=1)
print(tommorrow)
