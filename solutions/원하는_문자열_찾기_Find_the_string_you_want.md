# 원하는 문자열 찾기(Find the string you want)

## 문제 설명(Problem Description)
알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.
단, 알파벳 대문자와 소문자는 구분하지 않습니다.

## 접근 방법(Approach)
1. 대소문자를 구분하지 않으므로 대문자, 혹은 소문자로 통일시켜 확인해야 한다.
2. pat과 myString을 대문자로 변환한 뒤 pat이 myString에 속해있는지 확인한다.
3. 존재하면 1 아니면 0 리턴.

---
1. Since it is not case sensitive, you must check by unifying it to uppercase or lowercase.
2. Convert pat and myString to uppercase and check if pat belongs to myString.
3. If it exists, return 1, otherwise return 0.

   
## Python 코드(Python Code)
```
def solution(myString, pat):
    answer = 0
    pat = pat.upper()
    myString = myString.upper()
    if pat in myString:
        answer = 1
    return answer
```

## 기억할 점 (point)
문자열을 함수로 변환시킨 후에는 결과를 변수에 다시 저장해야 한다.


[뒤로 가기](../README.md)(Go back)
