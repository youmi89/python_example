# 리스트 복습
# 숫자, 문자에도 사용가능
# 순서가있는 형태를 시퀀스
# 슬라이싱 :뒤에 있는 숫자는 문자열로 인식하지 않는다
# 인덱싱은 나열된순서를 0부터 나열하는 방법
# -1 입력하면 제일 끝의자리 숫자를 가져온다

# ex
b = [1, "2", "good", 4, [1, 2, 3]]
c = [1, "2", "good", 4, [1, 2, 3, [123, "good"], 31], 2]
# good라는 문자열을 인덱싱 기법으로 추출
# 슬라이싱 기법을 통해 [123,"good"] 을 추출

print(c[4][3][1])
print(c[4][3][0:2])

# stack (후입선출)
# Queve (선입선출)


a = [1, 2, 3, "good"]
a[0] = 3
print(a)

a[3] = "aaaa"
print(a)
# 스트링의 문자열값을 새로운 대체형으로 특정문자는 바꿀수 없다
# 문자열의 전체는 바꿀수 있다.
# 중복이 허용


# clear() < 리스트안에있는 데이터만 삭제한다
# copy < 카피

a = []

a.append([1, 2, 3])
print(a)
a.clear()
print(a)

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(b)

# count
a = [1, 2, 3, "okay", 1, 1, 1]
print(a.count(1))

b = [1, 2, 3, [1, 2, 3, 1]]
print(b.count(1))
b.count(4)
print(b[3][2])  # <3을 추출하는

print(b.count(1) + b[3].count(1))
# <자동정렬 Shift + Alt + F

# extend
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
# [1,2,3,4,5,6,7,8]
print(a+b)
c = "good"
b.extend(c)
print(b)

# insert(인덱스, 값) #append는 뒤에 추가
a = [1, 2, 3, 4, 5]
# 중간에 끼워넣기
# 중간에 넣을경우 append
a.insert(0,0)
print(a)
# pop() 제일 끝에 있는 값 추출
# 리스트값이 비어있을경우 에러가 뜸 >pop from empty list
b = a.pop()
print(a)
# 리스트안에 데이터값이 1개 이상이면 추출
if len(a) >= 1:
    a.pop()
else:
    print("리스트가 비어있습니다.")

# remove 
# (값을 찾아서 지워버린다)
# 왼쪽부터 (참인것부터) 지운다
c = [1, 2, 3, 1, 1]
c.remove(1)
print(c) # [2, 3, 1, 1]
c.remove(1)
print(c) # [2, 3, 1]

fruit = ["사과", "딸기", "바나나", "낑깡"]
fruit.insert(1, "포도")
print(fruit) # insert

fruit = fruit.pop(4)
print(fruit) # pop

#fruit = fruit.remove("딸기")
#print(fruit)  왜 안될까...

# reveres < 뒤집는걸 말함 1,2,3 > 3,2,1
# 리버스는 담아도 변수에는 아무것도 없다
a = [1, 2, 3, 4, 5] 
# < a.reverse <이렇게 쓰는걸 권장하진 않는다.(원본훼손)
# reverse vs reversed
d = (list(reversed(a))) # <<추천
print(a)
print(d)

# sort 
# sorted < 기능
# c = [1, 2, 3, 4, 5]
# sorted(c, revers=False)
# x = list(soted(c, reverse=Trud))
# print(x)

# 문제 1
#1단계: 초기 도서 목록 생성하기
#books 리스트에 다음 5권의 책을 추가하세요: "파이썬 기초", "데이터 과학 입문", "알고리즘의 이해", "머신러닝 실전", "파이썬 기초"
#books 리스트를 출력하세요.
books = ["파이썬기초", "데이터과학입문", "알고리즘의이해", "머신러닝의실전", "파이썬기초"]
print(books.count("파이썬기초"))

# 문제 2
#2단계: 책 목록 관리하기
#목록에서 "파이썬 기초"가 몇 권 있는지 확인하세요.
#"웹 개발의 시작"이라는 책을 목록 끝에 추가하세요.
#"데이터베이스 설계"라는 책을 3번째 위치에 삽입하세요.
#새로운 책 리스트 new_books를 만들고 ["인공지능 개론", "클라우드 컴퓨팅"]을 포함시킨 후, books 리스트에 추가하세요. (extend 활용)
#수정된 books 리스트를 출력하세요.

books.insert(5, "웹계발의시작")
print(books)

books.insert(2, "데이터베이스설계")
print(books)

new_books = "인공지능개론", "클라우드컴퓨링"
books.extend(new_books)
print(f"여러책 추가 후: {books}")

# 문제 3
#3단계: 책 제거 및 관리하기
#목록에서 첫 번째로 등장하는 "파이썬 기초"를 제거하세요.
#리스트의 마지막 책을 빼내어 변수 last_book에 저장하고, 이 책을 출력하세요.
#책 목록을 알파벳 순으로 정렬하세요.
#정렬된 목록을 역순으로 뒤집으세요.
#수정된 books 리스트를 출력하세요.

books.remove("파이썬기초")
print(f"파이썬기초 제거 후: {books}")

last_books = books.pop()
print(f"빼낸 마지막 책: {last_books}")
print(f"책 빼낸 후: {books}")

books.sort()
print(f"정렬 후: {books}")
print(f"역순 정렬 후: {books}")

# 문제 4
# 4단계: 도서 목록 분석하기
# 슬라이싱을 사용하여 books 리스트의 처음 3권을 top_books라는 새 리스트에 저장하세요.
# books 리스트에서 2번째부터 5번째까지의 책들을 역순으로 reversed_selection이라는 새 리스트에 저장하세요.
# top_books와 reversed_selection을 출력하세요.
# books 리스트를 완전히 비우고 출력하세요.

top_books = books[0:3] # <처음부터 두번째 인덱스까지 가능
print(f"처음 3권: {top_books}")

reversed_selection = books[1:5][::-1]
print(f"2~5번째 책 역순: {reversed_selection}")

# 튜플(tuple)생성 () 를 사용, 
# 선언한 데이터는 삽입,수정할수 없다
# 읽고 사용하는것까지만 가능
# 여러가지 타입을 정할수 있다
a = (1,2,3)
b = [1,2,3]
print(type(a))

#print(a[3])
# 인덱싱 기능 사용가능

b = a[0:2] # 슬라이스 기능 사용가능
print(b)

# a[3] = "good" # < 수정이 불가능 (불변함)

numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)
print(numbers.count(5)) 
print(numbers.index(5)) 
