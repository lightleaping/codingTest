# A 강조하기(Emphasizing A)

## 문제 설명(Problem Description)
문자열 myString이 주어집니다. myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.

## 접근 방법(Approach)
1. 규칙에 따라 저장하여 리턴할 새로운 문자열 answer 생성.
2. for문으로 myString을 한 글자씩 가져온다.
3. if문으로 for문의 글자가 소문자 'a'와 일치하면 'A'로 변환하여 answer에 추가, 대문자 'A'이거나 'a'가 아닌 소문자이거나 공백인 경우 그대로 answer에 추가, 'A'가 아닌 대문자의 경우 소문자로 변환하여 answer에 추가.
4. return answer

---

1. Create a new string answer to save and return according to the rule.
2. Bring myString to the for statement one letter at a time.
3. If the letter of the for statement matches the lowercase 'a' in the if statement, it is added to answer by converting it to 'A', if it is lowercase or blank, then it is added to answer as it is, if it is a capital letter 'A', or if it is a non-A capital letter, it is converted to lowercase and added to answer.
4. return answer
   
## Python 코드(Python Code)
```
def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a':
            answer += 'A'
        elif i == 'A' or i.islower() or i == ' ':
            answer += i
        elif i.isupper():
            answer += i.lower()
    return answer
```

## 기억할 점 (point)
- 주어진 문자열이 대문자인지 확인하는 메서드: 문자열.isupper()
- 주어진 문자열이 소문자인지 확인하는 메서드: 문자열.islower()

[뒤로 가기](../README.md)(Go back)
