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

IndexError: list index out of range
IndexError: string index out of range

홀수번째 인덱스 == 인덱스가 홀수인 경우(1, 3, ...)

파이썬 얕은 복사(Shallow Copy)와 깊은 복사(Deep Copy)
- 얕은 복사 (Shallow Copy)
: 원본 객체의 참조만 복사. 중첩된 객체(리스트, 딕셔너리 등)는 원본과 공유.
내부 요소가 변경되면 원본에도 영향을 미친다.
: copy.copy(), list.copy()
: 객체의 크기가 크고 중첩된 구조가 없을 때, 원본과 일부 데이터를 공유하고 싶을 때

- 깊은 복사 (Deep Copy)
: 원본과 완전히 독립적인 복사본을 생성. 내부 리스트(중첩 객체)까지 새로운 객체로 복사.
복사본을 변경해도 원본에는 영향을 주지 않는다.
: copy.deepcopy()
: 원본과 완전히 독립적인 객체를 만들고 싶을 때, 중첩된 리스트, 딕셔너리 같은 복잡한 구조를 복사할 때
