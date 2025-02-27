# 간단한 식 계산하기 Calculate simple expressions

## 문제 설명(Problem Description)
문자열 binomial이 매개변수로 주어집니다. binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

## 접근 방법(Approach)
1. 변수 a, op, b 생성. 각각 음이 아닌 정수, 중간에 들어간 기호, 음이 아닌 정수 할당.
2. for문으로 인덱스 i를 이용해 binomial의 한 글자씩 순회시켜 a에 추가적으로 저장,한다.
3. 공백 문자가 나오면 i 값을 다른 변수 count에 저장, for문을 탈출한 뒤 

---

1. 
   
## Python 코드(Python Code)
```

```

## 기억할 점 (point)
Python의 for 문에서 문자열을 순회하면 한 글자씩 접근할 수 있다.
