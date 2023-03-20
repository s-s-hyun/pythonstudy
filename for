#for in <collection>(집합의 모음)
# <loop body>

for v1 in range(10):
    print('v1 is :', v1)

print()

for v2 in range(1, 11):
    print('v2 is :', v2)

print()

for v3 in range(2, 11, 2):
    print('v3 is  :', v3)

print()

sum1 = 0

for a in range(1,1001):
    sum1 += a

print('sum1 is :', sum1)

print('1000까지의 4의 배수의 합 =', sum(range(4,1001,4)))

# print(type(range(1,11)))

#Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
#iterable 리턴 함수 : range, reversed, enuerate, filter, map, zip

names = ['kim', 'park', 'cho', 'lee', 'yoo']

for n in names:
    print('You are :', n)

lotto_number = [11, 19, 21, 28, 36, 37]

for n in lotto_number:
    print('Currnet number :', n)

word = "beautiful"

for s in word:
    print('word :', s)

my_info = {
    "name": 'lee',
    "Age": 33,
    "City": 'Seoul'
}

for k in my_info:
    print('key :', my_info.get(k))
 
for v in my_info.values():
    print('values :', v)

#if + for
name = 'fineApplE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 5]

for num in numbers:
    if num == 34:
        print('find : 34')
        break
    else:
        print('not find :', num)

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type:", v, type(v))
    print("multiplay by 2", v * 3)

# for - else

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 5]

for num in numbers:
    if num == 49:
        print("Found : 24")
        break
else:
    print('Not Found : 49')

for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i *j), end='')
    print()

name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 집합은 순서 X
