str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1))
print(len(str1))
print()

str1_tr1 = ''
str2_tr2 = str()

print(type(str1_tr1), len(str2_tr2))

# 이스케이프 문자 사용

print("I'm Boy")
print('I\'m Boy')

print('a \t b')
print('a \n b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'what\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = 'clikc \t Start!'
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
r_s1 = r'D:\python\test'
print(r_s1)
print()

# 멀티라인 입력 역슬레시 사용
m_str = \
'''
string
Multi line
Test
'''

print(m_str)

# 문자열 연산
s_1 = "python"
s_2 = "Apple"
s_3 = "How are you doing"
s_4 = "Seoul Deajeon"

print(s_1 * 2)
print('y' in s_1)
print('z' in s_1)
print('P' not in s_2)

# 문자열 형 변환
print(str(66), type(str(66)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha)
print("capitalize: ", s_1.capitalize())
print("endsiwth?: ", s_2.endswith("e"))
print("replace", s_1.replace("thon", ' good')) #이 쉑 중요
print("sorted:", sorted(s_1))
print("split: ", s_4.split(' '))

# 반복(시퀀스)
im_str = "Godd boy!"

print(dir(im_str)) #__iter__

# 출력
for i in im_str:
    print(i)

# 슬라이싱 연습
str_s1 = "Nice Python"

# print(len(str_s1))
print(str_s1[0:3]) # -1까지 나온다
print(str_s1[5:])
print(str_s1[:len(str_s1)]) #85행 참고
print(str_s1[:len(str_s1)-1])
print(str_s1[1:9:2])
print(str_s1[-5:]) #뒤에서부터
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1]) #음수는 뒤에서부터

#아스키 코드(또는 유니코드)
a = 'z'
print(ord(a))
print(chr(122))