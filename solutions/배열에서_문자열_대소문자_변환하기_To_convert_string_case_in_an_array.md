# 배열에서 문자열 대소문자 변환하기(To convert string case in an array)

## 문제 설명(Problem Description)
문자열 배열 strArr가 주어집니다. 모든 원소가 알파벳으로만 이루어져 있을 때, 배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로,
짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution 함수를 완성해 주세요.

## 접근 방법(Approach) // 작성중
1. 결과 배열을 저장할 answer 배열 생성한다.
2. 대소문자를 바꾼 문자열을 저장할 convert 빈 문자열을 생성한다.
3. for문을 이용하여 strArr의 길이만큼 반복시켜 strArr의 모든 인덱스를 거친다.
4. if문과 나머지 연산자를 이용하여 strArr 내부의 인덱스의 2로 나눈 나머지가 0인 경우(짝수 번째) 해당하는 인덱스의 문자열의 문자를 대문자로 변경하여 convert에 한 글자씩 추가하기 위해 for문을 이용한다.
5. for문이 종료된 이후에 convert를 answer에 추가한다.
6. convert를 빈 문자열로 초기화한다.
7. 인덱스의 나머지가 0이 아닌 경우 해당 인덱스의 문자열의 모든 문자를 소문자로 변경하여 convert에 한 글자씩 추가하기 위해 for문을 이용한다.
8. for문이 종료된 이후에 convert를 answer에 추가한다.
9. convert를 빈 문자열로 초기화한다.
10. return answer

---

1. 
   
## Python 코드(Python Code)
```

```

## 기억할 점 (point)
AttributeError: 'list' object has no attribute 'upper'
TypeError: 'str' object does not support item assignment (문자열은 불변, 문자열의 특정 문자만 변경 불가능. 새로운 문자열을 만들어야 함.)
(-> 문자열 슬라이싱, 리스트 변환 후 변경 후 문자열 변환, replace() 사용)
IndexError: list index out of range

[뒤로 가기](../README.md)(Go back)
