## 배열에서 문자열 대소문자 변환하기(To convert string case in an array)

AttributeError: 'list' object has no attribute 'upper'
리스트에는 upper 함수를 사용할 수 없다. upper 함수는 문자열 객체에만 사용 가능.

- map()을 사용하여 리스트 변환 가능
1.
words = ["hello", "world"]
upper_words = list(map(str.upper, words))
print(upper_words)  # ['HELLO', 'WORLD']

2.
[word.upper() for word in words]

- 정수(int): 불가능	-> str(num).upper() 로 변환 후 사용


TypeError: 'str' object does not support item assignment
(문자열은 불변, 문자열의 특정 문자만 변경 불가능. 새로운 문자열을 만들어야 함.)
(-> 문자열 슬라이싱, 리스트 변환 후 변경 후 문자열 변환, replace() 사용)

- 문자열 슬라이싱 이용
my_string = "hello"
new_string = "H" + my_string[1:]  # 첫 번째 문자 변경
print(new_string)  # "Hello"

- 리스트로 변환 후 변경하고 다시 문자열로 변환
my_string = "hello"

# 문자열을 리스트로 변환
char_list = list(my_string)
char_list[0] = "H"  # 리스트에서는 원소 변경 가능

# 리스트를 다시 문자열로 변환
new_string = "".join(char_list)
print(new_string)  # "Hello"

- replace() 사용
my_string = "hello"
new_string = my_string.replace("h", "H", 1)  # 첫 번째 "h"만 "H"로 변경
print(new_string)  # "Hello"


IndexError: list index out of range
IndexError: string index out of range

홀수번째 인덱스 == 인덱스가 홀수인 경우(1, 3, ...)
