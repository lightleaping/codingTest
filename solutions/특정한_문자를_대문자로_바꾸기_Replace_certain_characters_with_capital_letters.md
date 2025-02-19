# 특정한 문자를 대문자로 바꾸기(Replace certain characters with capital letters)

## 문제 설명(Problem Description)
영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때, my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

## 접근 방법(Approach)
1. for문으로 my_string의 문자들을 한 글자씩 alp의 문자와 일치하는지 확인한다.
2. for문 안의 if문으로 두 글자가 서로 일치하는 경우 대문자로 바꾸어 새로운 문자열에 추가, 일치하지 않는 경우 그대로 추가한다.
3. return 새로운 문자열.

---

1. Use a for statement to check whether the characters in my_string match the characters in alp one by one.
2. If two letters match in the if statement within the for statement, change them to uppercase and add them to a new string. If they do not match, add them as is.
3. return new string.
   
## Python 코드(Python Code)
```
def solution(my_string, alp):
    answer = ''
    for i in my_string:
        if i == alp:
            answer += i.upper()
        else:
            answer += i
    return answer
```

## 기억할 점 (point)
문자열.upper() -> 소문자를 대문자로 변경

[뒤로 가기](../README.md)(Go back)
