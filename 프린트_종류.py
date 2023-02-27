\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

### 3가지 FORMAT PRACTICES

x = 50
y = 100
text = 308256565
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum=%d' % (n, text, (x + y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, sum={sum}' .format(n=n, s=text, sum=x+y) 
print(ex2)

# 출력3 F string 이게 진짜 편함
ex3 = f'n = {n}, s = {text}, sum={x+y}'
print(ex3)

print(f'n = {n}, s = {text}, sum={x+y}')

# 구분기호
m = 100000000

print(f'm : {m:,}')
print(f'{m:,}')

print()
print()

# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽

t = 20

print(f't : {t:10}')
print(f't center : {t:^10}')
print(f't left : {t:<10}')
print(f't right : {t:>10}')

print()
print()

print(f't center : {t:-^10}')
print(f't center : {t:#<50}')
